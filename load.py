from typing import Callable
import conditions
import actions
import inspect


def load_conditions() -> dict[str, Callable[..., bool]]:
    return {
        module_name: module.check
        for (module_name, module) in inspect.getmembers(conditions, inspect.ismodule)
    }


def load_actions() -> dict[str, Callable[..., None]]:
    return {
        module_name: module.run
        for (module_name, module) in inspect.getmembers(actions, inspect.ismodule)
    }
