from guesslang import Guess
text = "<b>Guidlines for Surveys</b>: 1)Get Specific 2)Avoid 1)Ambiguious? 2)Double-Barreled ?<div>3)Negative Words 4)Bias &nbsp;*Better to reuse then reinvent</div><div>Organizing Survey:1)include instructions 2)Group ?s into sections with similar topic/ideas</div><div>3)Leave for end 1)sensitive qs 2)demographic qs &nbsp; 4)consider length in design.</div><div><b>Experiment vs Survey: </b>A user experiment systematically tests how different system aspects (manipulations) influence the users? experience and behavior (observations).</div><div>A survey systematically tests how certain aspects of the user (observations) influence the users? experience and behavior (observations)</div><div><br></div>"
name = Guess().language_name(text)
print ("Hipy", name)
