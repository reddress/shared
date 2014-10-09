import odswriter as ods

with ods.writer(open("out.ods", "wb")) as odsfile:
    odsfile.writerow(['123456A'])
