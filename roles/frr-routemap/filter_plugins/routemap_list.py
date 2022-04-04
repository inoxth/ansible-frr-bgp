import re

def routemap_exists(lists, action, rmindex):
    for line in lists:
        if re.search("^route-map [^ ]+ " + str(action) + " " + str(rmindex) + "$", line):
            return True
    return False

def routemap_list(lists, rmindex):
    output = []
    found_start = False
    for line in lists:
        if found_start:
            if (line == "exit" or line == "!"):
                break
            output.append(line)
        if re.search("^route-map [^ ]+ [^ ]+ " + str(rmindex) + "$", line):
            found_start = True
    return output

def routemap_cleanup(lists, configure):
    output = []
    for line in lists:
        sequences = re.findall("^route-map [^ ]+ [^ ]+ ([0-9]+)$", line)
        if len(sequences) > 0:
            exists = False
            for item in configure:
                if str(item["sequence"]) == str(sequences[0]):
                    exists = True
                    break
            if not exists:
                output.append(line)
    return output

class FilterModule(object):
    def filters(self):
        return {
          'routemap_exists': routemap_exists,
          'routemap_list': routemap_list,
          'routemap_cleanup': routemap_cleanup
        }
