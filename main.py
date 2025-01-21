import load
import json


def main():
    conditions = load.load_conditions()
    actions = load.load_actions()
    with open("config.json") as f:
        config = json.load(f)
    for check in config["checks"]:
        condition = conditions[check["condition"]["name"]]
        if condition(
            **{
                name: arg
                for (name, arg) in check["condition"].items()
                if name != "name"
            }
        ):
            actions_to_run = [
                (actions[action["name"]], action) for action in check["actions"]
            ]
            for action, params in actions_to_run:
                action(
                    **{name: arg for (name, arg) in params.items() if name != "name"}
                )
    return 0


if __name__ == "__main__":
    main()
