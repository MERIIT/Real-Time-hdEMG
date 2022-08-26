import helpers.environment_variables as env
from helpers.communication import receive_signal, send_signal, get_emg_client
from helpers.prediction import get_prediction, int_to_volt
# from helpers.visualization import plot_force
import helpers.data_storage1 as storage

def main():
    client = get_emg_client(tcp_port=env.SS_TCP_PORT, hostname=env.SS_HOSTNAME)
    try:
        send_signal(client, env.SS_START_SIGNAL)
        while True:
            data = receive_signal(client)
            emg = int_to_volt(data)
            storage.add_recording(emg)
            # prediction = get_prediction(data)

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)
    finally:
        storage.persist_recordings()
        print("Stream Closed")
        send_signal(client, env.STOP_SIGNAL)
        client.close()


if __name__ == '__main__':
    main()
