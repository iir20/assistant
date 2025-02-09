import time

class Animation:
    @staticmethod
    def welcome(name):
        print(f"""
        ╔═╗╔╗╔╔═╗╦ ╦╔═╗╦╔═
        ║ ╦║║║║╣ ║║║╠═╣╠╩╗
        ╚═╝╝╚╝╚═╝╚╩╝╩ ╩╩ ╩
        Welcome back, {name}!
        """)
        time.sleep(1)

    @staticmethod
    def thinking():
        frames = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        for frame in frames:
            print(f"\r{frame} Processing...", end="")
            time.sleep(0.1)
        print("\rDone!          ")