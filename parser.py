# BOOO!!!!


import json
from collections import defaultdict
from datetime import datetime
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog

# Dictionaries of the names for the label and author ID's
label_names = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
    9: "",
    10: ""
}

author_names = {}

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
    
# Asks user to give names to the label ID's, filling the dictionary
    ask_label_names(events)

def ask_label_names(events):
    label_window = tk.Toplevel(root)
    label_window.title("Enter Label Names")

    tk.Label(label_window, text="Enter names for labels:").pack(pady=10)

    entry_vars = {}
    for label_id in label_names.keys():
        frame = tk.Frame(label_window)
        frame.pack(pady=2)

        tk.Label(frame, text=f"Label {label_id}:").pack(side=tk.LEFT)
        entry_var = tk.StringVar()
        entry_vars[label_id] = entry_var
        entry = tk.Entry(frame, textvariable=entry_var)
        entry.pack(side=tk.LEFT)

    def save_labels():
        for label_id, entry_var in entry_vars.items():
            label_names[label_id] = entry_var.get()
        label_window.destroy()
        ask_author_names(events)

    tk.Button(label_window, text="Save", command=save_labels).pack(pady=10)

# Asks user to give names to the aurthor ID's, filling the dictionary
def ask_author_names(events):
    unique_author_ids = set(event['author_id'] for event in events if 'author_id' in event)

    author_window = tk.Toplevel(root)
    author_window.title("Enter Author Names")

    tk.Label(author_window, text="Enter names for authors:").pack(pady=10)

    entry_vars = {}
    for author_id in unique_author_ids:
        frame = tk.Frame(author_window)
        frame.pack(pady=2)

        tk.Label(frame, text=f"Author {author_id}:").pack(side=tk.LEFT)
        entry_var = tk.StringVar()
        entry_vars[author_id] = entry_var
        entry = tk.Entry(frame, textvariable=entry_var)
        entry.pack(side=tk.LEFT)

    def save_authors():
        for author_id, entry_var in entry_vars.items():
            author_names[author_id] = entry_var.get()
        author_window.destroy()
        process_events(events)

    tk.Button(author_window, text="Save", command=save_authors).pack(pady=10)

# Get the event titles and the number of events per label, date (month/year) and user
def process_events(events):
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

# Converts the label and author ID's to names from the dictionary
        label_id = event.get('label_id')
        if label_id in label_names:
            label_name = label_names[label_id]
            events_per_label[label_name] += 1

        author_id = event.get('author_id')
        if author_id in author_names:
            author_name = author_names[author_id]
            events_per_author[author_name] += 1

    plot_graphs()

# Takes the result from process_events and plots three graphs showing which labels, months and users have the most events tied to them
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
    plt.xlabel('Authors')
    plt.ylabel('Number of Events')
    plt.title('Number of Events per Author')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

root = tk.Tk()
root.title("TimeTree Event Parser")

btn_load = tk.Button(root, text="Load JSON File", command=load_json_file)
btn_load.pack(pady=20)

root.mainloop()
