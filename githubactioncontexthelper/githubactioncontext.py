"""
githubactioncontexthelper.githubactioncontext.py
~~~~~~~~~~~~~~~~

This exaple module contains classes that model economic supply and
demand curves and compute values such as equilibrium prices. 

It also serves as a demonstration for using type annotations and
abstract base classes in developing libraries intended for use in other
projects.
"""

import abc
from dataclasses import dataclass
from typing import Dict, Optional, Sequence, Tuple, TypeVar


import datetime
import json
from json import dumps
import os
import logging
import pickle
import codecs
from pathlib import Path

class Context(Dict):
    __context_variable_name = "github_action_context_variable_holder"

    def __init__(self):
        
        logging.debug("==============================")
        if self.__context_variable_name in locals():
            logging.debug("Environment context found in locals.")
            logging.debug(f"All env variables: {os.environ}")
            loading_context = locals().get(self.__context_variable_name)
        elif self.__context_variable_name in globals():
            logging.debug("Environment context not found. Initializing to empty.")
            logging.debug(f"All env variables: {os.environ}")
            self.update(globals().get(self.__context_variable_name))
        elif os.getenv(self.__context_variable_name) is not None:
            self.rehydrate(os.getenv(self.__context_variable_name))
            logging.debug(f"'{self.__context_variable_name}' environment variable found.")
            logging.debug(f"'{self.__context_variable_name}' == {self}")
        elif Path(self.__context_variable_name).exists():
            logging.debug("File found - reading values.")
            file_text = Path(self.__context_variable_name).read_text()
            self.rehydrate(file_text)
        else:
            logging.debug("Environment context not found. Initializing to empty.")
            logging.debug(f"All env variables: {os.environ}")
            loading_context = {}

        logging.debug("==============================")

        dict.__init__(self)

    def __getitem__(self, key):
        val = dict.__getitem__(self, key)
        return val

    def __setitem__(self, key, val):
        dict.__setitem__(self, key, val)

    def dehydrate(self):
        # encode returns bytes so it needs to be decoded to string
        pickled = codecs.encode(pickle.dumps(self), "hex").decode()
        return pickled

    def rehydrate(self, context_string):
        unpickled = pickle.loads(codecs.decode(context_string.encode(), "hex"))
        self.update(unpickled)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:        
        logging.debug("==============================")
        logging.debug(f"Current Context: {self.print_context()}")
        logging.debug("==============================")
        # The below is for use in GitHub Actions - so we can pass values from one script to another.

        context_serialization = self.dehydrate()
        if (os.getenv('GITHUB_ACTION') is not None):
            print(f'::set-output name={self.__context_variable_name}::{context_serialization}')

        os.environ[self.__context_variable_name] = context_serialization
        Path(self.__context_variable_name).write_text(context_serialization)

    def print_context(self):
        print(self)
