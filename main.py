import threading
import time



def show_miku():
    import py_voice

def v_miku():
    import Live2d_conture
    
def main():
    thread1 = threading.Thread(target=show_miku)

    thread2 = threading.Thread(target=v_miku)

    thread1.start()

    thread2.start()

    thread1.join()

    thread2.join()

if __name__ == "__main__":
    main()
