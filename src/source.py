import os
from contextlib import contextmanager
from dataclasses import dataclass, field
from typing import List, Mapping
import logging
import subprocess

log = logging.getLogger(__name__)

@dataclass
class Source:
    project: "Project"
    file_path: str


    def clip(self, output_filename:str, start_timecode: str, end_timecode: str, **metadata) -> "Clip":
        c: Clip = Clip(self, output_filename=output_filename, start_timecode=start_timecode, end_timecode=end_timecode, metadata=metadata)
        c.validate()
        self.project.clips.append(c)
        return c


def timestamp_to_seconds(timestamp:str)->int:
    h,m,s = [int(x) for x in timestamp.split(":")]
    return s + m * 60 + h * 3600

@dataclass
class Clip:
    source: Source
    output_filename: str
    start_timecode: str
    end_timecode: str
    metadata: Mapping[str,str]

    def validate(self):
        assert timestamp_to_seconds(self.start_timecode) < timestamp_to_seconds(self.end_timecode), f"This clip is invalid because it ends before it starts: {self.output_filename}"
        assert not (" " in self.output_filename), f"Output filename should not contain any whitespace: {self.output_filename}"
        assert self.output_filename.endswith(".mp4"), f"invalid filename: {self.output_filename}."
        return True

    def extract(self, index_number:int, output_directory:str):
        assert os.path.exists(output_directory) and os.path.isdir(output_directory), f"{output_directory} should be a directory"

        full_filename = f"{self.source.project.project_name}.{index_number}.{self.output_filename}"
        output_file_path = os.path.join(output_directory, full_filename)

        if not os.path.exists(output_file_path):
            log.info(f"Extracting {self}")
            metadata_string = " ".join([f"-metadata {k}=\"{v}\"" for (k,v) in self.metadata.items()])
            command = ["ffmpeg", "-i", f"\"{self.source.file_path}\"", "-ss", self.start_timecode, "-to", self.end_timecode, "-async", "1",  metadata_string, f"\"{output_file_path}\""]
            log.info(f"Executing: {' '.join(command)}")
            output = subprocess.check_output(" ".join(command), shell=True)
            log.info(output)



def get_input_directory()->str:
    return os.environ["INPUT_DIRECTORY"]


def get_output_directory()->str:
    return os.environ["OUTPUT_DIRECTORY"]



@dataclass()
class Project:
    project_name: str
    clips: List["Clip"] = field(default_factory=list)

    @contextmanager
    def clip_maker(self, filename: str):
        file_path = os.path.join(get_input_directory(), filename)
        assert os.path.exists(file_path), f"Input file {file_path} does not exist."
        s = Source(project=self, file_path=file_path)
        yield s

        for c in self.clips:
            c.validate()

        for i, clip in enumerate(self.clips):
            clip.extract(output_directory=get_output_directory(), index_number=i)


@contextmanager
def project_maker(project_name:str):
    project = Project(project_name=project_name)
    yield project


