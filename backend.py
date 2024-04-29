
import platform
import json
import re
import os

def path_stuff(mcdir, subdir):
    ps = "/" if mcdir.count("/") > 0 else "\\"
    mcdir.rstrip(ps)
    for i in subdir: mcdir = mcdir + ps + i
    return mcdir

def get_versions(mcdir):
    mcdir = path_stuff(mcdir, ["versions"])
    return os.listdir(mcdir)

def start_version(mcdir, version):
    options = path_stuff(mcdir, ["versions", version, version + ".json"])
    with open(options, "r") as f: d = f.read()
    options = json.loads(d)
    args = ""
    if options.get("arguments"):
        options = options["arguments"]
        for i in options["game"]:
            if type(i) != str:
                allowed = False
                for j in i.get("rules"):
                    if j.get("features"):
                        allowed = False
                        break
                    if j.get("os"):
                        osv = platform.system().lower()
                        try:
                            osv = {"win32": "windows", "cygwin": "windows", "darwin": "osx"}[osv]
                        except KeyError: pass
                        if j["os"].get("name"):
                            if j["os"]["name"] != osv:
                                allowed = j["action"] == "allow"
                                if not allowed: break
                        if j["os"].get("arch"):
                            if j["os"]["arch"] != platform.machine():
                                allowed = j["action"] == "allow"
                                if not allowed: break
                        if j["os"].get("version"):
                            if not re.match(j["os"]["version"], platform.version()):
                                allowed = j["action"] == "allow"
                                if not allowed: break
                if not allowed: continue
                for j in i["value"]:
                    if i.count("$") > 0:
                        i = i.replace("$", "")
                        i = format_option(i)
                    args = args + " " + i
            if i.count("$") > 0:
                i = i.replace("$", "")
                i = format_option(i)
            args = args + " " + i
    return args


def format_option(s): return s

print(start_version("/home/fritz/.minecraft", "1.16.4"))

