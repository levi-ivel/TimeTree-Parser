import json
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Set label ID's to names
label_names = {
    1: "X",
    2: "X",
    3: "X",
    4: "X",
    5: "X",
    6: "X",
    7: "X",
    8: "X",
    9: "X",
    10: "X"
}

author_names = {
    ID_HERE: "X",
    ID_HERE: "X",
    ID_HERE: "X",
    ID_HERE: "X",
    ID_HERE: "X",
    ID_HERE: "X",
    ID_HERE: "X",
    ID_HERE: "X",
    ID_HERE: "X",
    ID_HERE: "X"
    }

events_per_month_year = defaultdict(int)
events_per_label = defaultdict(int)
events_per_author = defaultdict(int)
event_titles = []

# Loads the TimeTree JSON file
def load_json_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return
    
    with open(file_path, 'r', encoding='utf-8') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return

    if 'events' not in data or not isinstance(data['events'], list):
        print("Error: JSON data does not contain a list of events under the key 'events'")
        return

    events = data['events']

# Goes trough all events and extracts the label ID, title and date (month/year) from each event
    for event in events:
        if not isinstance(event, dict):
            print(f"Error: Event data is not a dictionary: {event}")
            continue

        title = event.get('title', 'Untitled')
        event_titles.append(title)

        start_timestamp = event.get('start_at')
        if start_timestamp:
            start_datetime = datetime.fromtimestamp(start_timestamp / 1000)
            month_year = start_datetime.strftime('%B %Y')
            events_per_month_year[month_year] += 1

        label_id = event.get('label_id')
        if label_id in label_names:
            label_name = label_names[label_id]
            events_per_label[label_name] += 1

        author_id = event.get('author_id')
        if author_id in author_names:
            author_name = author_names[author_id]
            events_per_author[author_name] += 1

    plot_graphs()

# Takes label and timestamp data and plots an ordered graph
def plot_graphs():
    sorted_labels = sorted(events_per_label.items(), key=lambda x: x[1], reverse=True)
    labels = [item[0] for item in sorted_labels]
    counts_labels = [item[1] for item in sorted_labels]

    sorted_months = sorted(events_per_month_year.items(), key=lambda x: x[1], reverse=True)
    months = [item[0] for item in sorted_months]
    counts_months = [item[1] for item in sorted_months]

    sorted_authors = sorted(events_per_author.items(), key=lambda x: x[1], reverse=True)
    authors = [item[0] for item in sorted_authors]
    counts_authors = [item[1] for item in sorted_authors]

    plt.figure(figsize=(10, 5))
    plt.bar(labels, counts_labels, color='skyblue')
    plt.xlabel('Labels')
    plt.ylabel('Number of Events')
    plt.title('Number of Events per Label')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.bar(months, counts_months, color='skyblue')
    plt.xlabel('Month Year')
    plt.ylabel('Number of Events')
    plt.title('Number of Events per Month and Year')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.figure(figsize=(10, 5))
    plt.bar(authors, counts_authors, color='skyblue')
    plt.xlabel('authors')
    plt.ylabel('Number of Events')
    plt.title('Number of Events per author')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

root = tk.Tk()
root.title("TimeTree Event Parser")

btn_load = tk.Button(root, text="Load JSON File", command=load_json_file)
btn_load.pack(pady=20)

root.mainloop()
