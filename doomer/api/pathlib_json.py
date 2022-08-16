import pathlib
import json


class PathJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, pathlib.WindowsPath) or isinstance(o, pathlib.PosixPath):
            return str(o)
        return json.JSONEncoder.default(self, o)


class PathJSONDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.__object_hook, *args, **kwargs)

    def __object_hook(self, o):
        for key in o.keys():
            o[key] = pathlib.Path(o[key])
        return o
