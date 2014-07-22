import clever

clever.set_token("DEMO_TOKEN")
sections = clever.Section.all()
sum([len(s.students) for s in sections])/float(len(sections))
