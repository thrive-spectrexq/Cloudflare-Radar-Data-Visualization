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

    try:
        data2 = endpoint2.fetch_data()
        print("Data from Endpoint 2:")
        print(data2)
    except Exception as e:
        print(f"Error fetching data from Endpoint 2: {e}")

    try:
        data3 = endpoint3.fetch_data()
        print("Data from Endpoint 3:")
        print(data3)
    except Exception as e:
        print(f"Error fetching data from Endpoint 3: {e}")

    try:
        data4 = endpoint4.fetch_data()
        print("Data from Endpoint 4:")
        print(data4)
    except Exception as e:
        print(f"Error fetching data from Endpoint 4: {e}")

    try:
        data5 = endpoint5.fetch_data()
        print("Data from Endpoint 5:")
        print(data5)
    except Exception as e:
        print(f"Error fetching data from Endpoint 5: {e}")

    return data1, data2, data3, data4, data5


def save_data(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f)


def load_data(filename):
    if os.path.exists(filename):
        with open(filename, "r") as f:
            return json.load(f)
    return None


def visualize_data(data):
    if data:
        # Example visualization for Endpoint 1
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
    visualize_data(loaded_data1)
    visualize_data(loaded_data2)
    visualize_data(loaded_data3)
    visualize_data(loaded_data4)
    visualize_data(loaded_data5)
