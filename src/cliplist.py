import logging
from src.source import project_maker


def main():
    with project_maker("mark_steele") as p:
        with p.clip_maker("1.mp4") as s:
            s.clip("education1.mp4", "00:20:25", "0:21:33", title="education 1")
            s.clip("education2.mp4", "00:23:28", "0:24:00", title="Why where you chosen for the job")
            s.clip("where_did_life_take_you.mp4", "0:24:00", "00:29:59", title="Mark's book voucher")
            s.clip("interest_in_weapons.mp4", "00:30:09", "0:30:50", title="He knew a lot about weapons for some inexplicable reason")
            s.clip("interrogating.mp4", "00:30:58", "0:31:22", title="He used to interrogate scientists")
            s.clip("5g_activates_pathogen.mp4", "00:35:55", "0:36:26", title="Mark links 5G to the current pandemic")
            s.clip("fcc_reg1.mp4", "00:37:45", "0:38:36", title="Mark thinks that the Leafnut device is not FCC approved")
            s.clip("fcc_reg2.mp4", "00:39:28", "0:39:52", title="Mark thinks the FCC registration was forged")
            s.clip("fcc_reg3.mp4", "00:40:30", "0:41:28", title="Mark rants more about the FCC")
            s.clip("dipole_antenna.mp4", "00:41:43", "0:42:03", title="Toon held a dipole antenna")
            s.clip("leafnut.mp4", "00:42:09", "0:43:35", title="Mark thinks it's impossible to buy a LeafNut")
            s.clip("challenge.mp4", "00:46:40", "0:47:02", title="Mark's challenge to McToon")
            s.clip("what_is_a_high_gain_antenna.mp4", "00:51:16", "0:52:11", title="I ask Mark what is meant by a high-gain antenna?")
            s.clip("what_is_a_monopole.mp4", "00:53:29", "0:53:58", title="Mark says that a monpole isn't a kind of antenna")
            s.clip("what_is_a_high_gain_antenna.mp4", "00:54:01", "0:54:27", title="Mark defines a high-gain antenna")
            s.clip("that_blob.mp4", "00:56:53", "0:57:28", title="Mark thinks that varnishing an antenna would stop it working")
            s.clip("lenses.mp4", "01:03:41", "1:04:46", title="Mark explains how lenses work")
            s.clip("the_main_technical_parameter_for_5g_0.mp4", "01:06:43", "1:07:11", title="Mark claims that the main technical parameter for 5G is focussed energy in air")
            s.clip("the_main_technical_parameter_for_5g_1.mp4", "01:07:34", "1:08:05", title="Mark talks a bit more about technical parameters")
            s.clip("if_5g_just_a_weapon.mp4", "01:09:38", "1:09:54", title="Mark syas that 5g 5g phones don't exist")
            s.clip("if_5g_just_a_weapon.mp4", "01:10:40", "1:11:45", title="Mark explains why 5g phones cannot exist")
            s.clip("how_does_it_kill.mp4", "01:13:34", "1:13:52", title="Ionization is lethal!")
            s.clip("what_is_the_effect_on_my_Body.mp4", "01:13:34", "1:14:16", title="Mark says that 5G can vaporize you!")
            s.clip("9-11_0.mp4", "01:15:10", "1:15:25", title="Mark says that the destruction of the twin towers was caused by 5g!")
            s.clip("9-11_1.mp4", "01:17:16", "1:18:09", title="Mark talks more about how 5g destroyed the twin towers!")
        with p.clip_maker("2.mp4") as s:
            s.clip("toons_agenda.mp4", "00:04:24", "00:05:11", title="Mark says he enjoyed taking the piss out of McToon")
            s.clip("who_is_mctoon.mp4", "00:06:16", "00:06:30", title="Mark says McToon is taking him out of context")
            s.clip("toons_agenda.mp4", "00:04:24", "00:05:11", title="Mark says he enjoyed taking the piss out of McToon")
            s.clip("toons_organization.mp4", "00:06:46", "00:07:07", title="Mark suggests that Toon might be connected")
            s.clip("cabal.mp4", "00:09:29", "00:09:42", title="Mark talks about the Cabal")
            s.clip("prophecy.mp4", "00:11:09", "00:12:31", title="Mark says that he has evidence that five cities were destroyed in Korea")
            s.clip("what_other_products.mp4", "00:17:03", "00:17:47", title="I asked Mark what other products her worked on")
            s.clip("marks_impossible_carbon_cracker.mp4", "00:20:58", "00:21:42", title="Mark claims that he invented a machine that could break down carbon dioxide")
            s.clip("spectrum_analyser.mp4", "00:25:36", "00:26:47", title="Mark claims that he measured the output of the harvard leafnode with a spectrum analyzer")
            s.clip("non_ionizing_radiation.mp4", "00:25:36", "00:30:40", title="Mark defines non-ionizing radiation")
            s.clip("ionization.mp4", "00:30:42", "00:31:05", title="Mark defines what an ion is")
            s.clip("ionization.mp4", "00:31:19", "00:32:31", title="Mark is confused about radiation")
            s.clip("ionization.mp4", "00:32:29", "00:32:58", title="Mark is confused about radiation")
            s.clip("ionization.mp4", "00:32:58", "00:34:40", title="Mark is confused about ionization")
            s.clip("why_are_5g_phones_faster.mp4", "00:36:03", "00:36:53", title="Mark does not believe that 5g phones exist")
            s.clip("how_does_5g_kill.mp4", "00:38:36", "00:39:18", title="Mark thinks 1kw would cause you to die")
            s.clip("inverse_square_law.mp4", "00:40:13", "00:40:57", title="Mark explains why the inverse square law does not apply to 5g")
            s.clip("5g_targeting.mp4", "00:43:22", "00:43:53", title="Mark Mark explains how the targeting works")
            s.clip("5g_is_not_targeted.mp4", "00:44:23", "00:45:20", title="Lasers in the jungle?")
            s.clip("how_many_lamp_posts_would_it_take_to_kill_a_person.mp4", "00:54:23", "00:54:36", title="I ask Mark how many lamp-posts it would take to kill a person?")
            s.clip("grenfell_tower_disaster.mp4", "00:55:39", "00:56:28", title="Mark links the Grenfell tower disaster to 5g and smart-meters?")
            s.clip("why_not_just_shoot_everybody.mp4", "00:57:12", "00:57:55", title="I ask Mark why the cabal goes to so much effort when they could just shoot everybody?")
            s.clip("capacitor.mp4", "00:59:27", "01:01:19", title="I ask Mark why he's worried about the leafnut capacitor")
            s.clip("capacitor.mp4", "00:59:27", "01:01:19", title="More chatter about capacitors")
            s.clip("911_again.mp4", "01:09:39", "01:11:31", title="Mark talks again about 9/11")
        with p.clip_maker("3.mp4") as s:
            s.clip("matching_antennas_with_wavelength.mp4", "00:03:28", "00:07:08", title="I ask if it's true that antennas have to be tuned for a wavelength")
            s.clip("mark_offers_to_provide_evidence_that_nanoparticles_can_refelect_radiation.mp4", "00:08:49", "00:09:19", title="I ask Mark for some evidence")
            s.clip("mark_talks_about_the_telensa_curcuit.mp4", "00:13:11", "00:16:18", title="I ask Mark about the Telensa")
            s.clip("mctoon_fake_accounts.mp4", "00:28:28", "00:30:50", title="Kim Tate asks mark how he knows that McToon's followers are fake or satanists")
            s.clip("satanist_symbpols.mp4", "00:31:32", "00:32:19", title="Kim and Mark see symbols everywhere")
            s.clip("is_mark_being_persecuted_by_satan.mp4", "00:31:32", "00:32:19", title="Kim and Mark see symbols everywhere")
            s.clip("mc_toons_mental_problems.mp4", "00:33:21", "00:34:53", title="Mark says that McToon is insane, gay, etc")
            s.clip("mc_toons_mental_problems.mp4", "00:34:53", "00:36:02", title="Mark speculates what McToon's mental health problems might be")
            s.clip("mc_toons_mental_problems.mp4", "00:36:03", "00:36:32", title="Mark speculates what drungs McToon might be on")
            s.clip("who_is_paything_mctoon.mp4", "00:36:32", "00:37:16", title="Kim asks Mark if McToon is being paid to make content")
            s.clip("harvard_on_ebay.mp4", "00:37:16", "00:38:51", title="Kim asks Mark if the Harvard device can be bought on eBay")
            s.clip("steele_on_mcniel.mp4", "00:40:03", "00:41:01", title="Kim asks Mark to comment aobut McNeil's video")
            # Skipping loads
            s.clip("do_viruses_exist.mp4", "01:34:28", "01:34:38", title="I ask Mark if viruses exist")
            s.clip("wifi_causes_diabetes.mp4", "01:35:03", "01:35:47", title="Mark suggests that turning off wifi will cure diabetes")
            s.clip("wifi_causes_diabetes.mp4", "01:35:52", "01:37:23", title="Mark evedes showing evidence")
            s.clip("do_viruses_cause_disease.mp4", "01:37:49", "01:38:38", title="I ask Mark if viruses cause disease")
            s.clip("do_viruses_cause_disease.mp4", "01:39:00", "01:40:25", title="I ask Mark if viruses cause disease")
            s.clip("is_a_vrus_a_pathogen.mp4", "01:40:28", "01:41:01", title="I ask Mark if viruses are pathogens")
            s.clip("what_is_a_vaccine.mp4", "01:41:00", "01:42:07", title="I ask Mark to explain what a vaccine is")
            s.clip("which_vaccines_contain_tungsten.mp4", "01:42:12", "01:43:20", title="I ask mark why he thinks vaccines contain tungsten")
            # Skipping loads






if __name__ == "__main__":
    logging.basicConfig()
    logging.getLogger("").setLevel(logging.INFO)
    main()
