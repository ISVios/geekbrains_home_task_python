#!/usr/bin/env python3

""" task 1 2 """

def parse_log(pth_file):

    if pth_file:
        with open(pth_file,"r",encoding="utf-8") as file:
            for line in file:
                ip = line.split(" - - ")[0]
                rsp_and_pth = line.split('"')[1]
                rsp = rsp_and_pth.split()[0]
                pth = rsp_and_pth.split()[1]
                yield(ip, rsp, pth)


def find_spamer(parsed_log):
    
    if not parsed_log:
        return None
    
    db = {}

    for log in  parsed_log:
        if not db.get(log[0]):
            db[log[0]] = {"count":1, "files":set([log[2]])}
        else:
            db[log[0]]["count"] += 1
            db[log[0]]["files"].add(log[2])

    return max(db.items(), key=lambda x: x[1]["count"])


if __name__ == "__main__":
   parsed_log = parse_log("./nginx_logs.txt")
   spamer = find_spamer(parsed_log) 
   
