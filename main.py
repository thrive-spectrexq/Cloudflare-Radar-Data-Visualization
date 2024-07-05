import endpoint1
import endpoint2
import endpoint3
import endpoint4
import endpoint5
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import json
import os


def fetch_data():
    try:
        data1 = endpoint1.fetch_data()
        print("Data from Endpoint 1:")
        print(data1)
    except Exception as e:
        print(f"Error fetching data from Endpoint 1: {e}")
        data1 = None

    try:
        data2 = endpoint2.fetch_data()
        print("Data from Endpoint 2:")
        print(data2)
    except Exception as e:
        print(f"Error fetching data from Endpoint 2: {e}")
        data2 = None

    try:
        data3 = endpoint3.fetch_data()
        print("Data from Endpoint 3:")
        print(data3)
    except Exception as e:
        print(f"Error fetching data from Endpoint 3: {e}")
        data3 = None

    try:
        data4 = endpoint4.fetch_data()
        print("Data from Endpoint 4:")
        print(data4)
    except Exception as e:
        print(f"Error fetching data from Endpoint 4: {e}")
        data4 = None

    try:
        data5 = endpoint5.fetch_data()
        print("Data from Endpoint 5:")
        print(data5)
    except Exception as e:
        print(f"Error fetching data from Endpoint 5: {e}")
        data5 = None

    return data1, data2, data3, data4, data5


def save_data(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)


def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return None


def visualize_data(endpoint, data):
    if data:
        if endpoint == 1:
            # Visualization for Endpoint 1
            timestamps = data["result"]["human"]["timestamps"]
            mobile = data["result"]["human"]["mobile"]
            desktop = data["result"]["human"]["desktop"]
            other = data["result"]["human"]["other"]

            df = pd.DataFrame(
                {
                    "timestamps": pd.to_datetime(timestamps),
                    "mobile": [float(i) for i in mobile],
                    "desktop": [float(i) for i in desktop],
                    "other": [float(i) for i in other],
                }
            )

            plt.figure(figsize=(12, 6))
            sns.lineplot(data=df, x="timestamps", y="mobile", label="Mobile")
            sns.lineplot(data=df, x="timestamps", y="desktop", label="Desktop")
            sns.lineplot(data=df, x="timestamps", y="other", label="Other")
            plt.title("Traffic Distribution Over Time")
            plt.xlabel("Time")
            plt.ylabel("Percentage")
            plt.legend()
            plt.show()

        elif endpoint == 2:
            # Visualization for Endpoint 2
            timestamps = data["result"]["timestamps"]
            bytes_in = data["result"]["bytesIn"]
            bytes_out = data["result"]["bytesOut"]

            df = pd.DataFrame(
                {
                    "timestamps": pd.to_datetime(timestamps),
                    "bytes_in": [float(i) for i in bytes_in],
                    "bytes_out": [float(i) for i in bytes_out],
                }
            )

            plt.figure(figsize=(12, 6))
            sns.lineplot(data=df, x="timestamps", y="bytes_in", label="Bytes In")
            sns.lineplot(data=df, x="timestamps", y="bytes_out", label="Bytes Out")
            plt.title("Netflows Over Time")
            plt.xlabel("Time")
            plt.ylabel("Bytes")
            plt.legend()
            plt.show()

        elif endpoint == 3:
            # Visualization for Endpoint 3
            timestamps = data["result"]["timestamps"]
            attacks = data["result"]["attacks"]

            df = pd.DataFrame(
                {
                    "timestamps": pd.to_datetime(timestamps),
                    "attacks": [float(i) for i in attacks],
                }
            )

            plt.figure(figsize=(12, 6))
            sns.lineplot(data=df, x="timestamps", y="attacks", label="Attacks")
            plt.title("Layer 7 Attacks Over Time")
            plt.xlabel("Time")
            plt.ylabel("Number of Attacks")
            plt.legend()
            plt.show()

        elif endpoint == 4:
            # Visualization for Endpoint 4
            locations = data["result"]
            df = pd.DataFrame(locations)

            plt.figure(figsize=(12, 6))
            sns.barplot(data=df, x="location", y="count")
            plt.title("Top DNS Locations")
            plt.xlabel("Location")
            plt.ylabel("Count")
            plt.show()

        elif endpoint == 5:
            # Visualization for Endpoint 5
            outages = data["result"]
            df = pd.DataFrame(outages)

            plt.figure(figsize=(12, 6))
            sns.barplot(data=df, x="start_time", y="duration", hue="region")
            plt.title("Outages Over Time")
            plt.xlabel("Start Time")
            plt.ylabel("Duration")
            plt.legend()
            plt.show()


if __name__ == "__main__":
    # Fetch data from all endpoints
    data1, data2, data3, data4, data5 = fetch_data()

    # Save data to JSON files
    save_data(data1, "data/data_endpoint1.json")
    save_data(data2, "data/data_endpoint2.json")
    save_data(data3, "data/data_endpoint3.json")
    save_data(data4, "data/data_endpoint4.json")
    save_data(data5, "data/data_endpoint5.json")

    # Load data from JSON files
    loaded_data1 = load_data("data/data_endpoint1.json")
    loaded_data2 = load_data("data/data_endpoint2.json")
    loaded_data3 = load_data("data/data_endpoint3.json")
    loaded_data4 = load_data("data/data_endpoint4.json")
    loaded_data5 = load_data("data/data_endpoint5.json")

    # Visualize the loaded data
    visualize_data(1, loaded_data1)
    visualize_data(2, loaded_data2)
    visualize_data(3, loaded_data3)
    visualize_data(4, loaded_data4)
    visualize_data(5, loaded_data5)
