from sqlsetup import connect, run, commit, tbl, close

connect('sakila')
run("SELECT * FROM address")
tbl()
close()

connect('mydb')
run("SELECT * FROM player")
tbl()
run("DESC player")
close()

