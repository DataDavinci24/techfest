import tkinter as tk
from tkinter import filedialog
import os
import random
class FindRightResumeApp:
    def __init__(self, master):
        self.master = master
        master.title("Find the Right Resume!")

        self.description_label = tk.Label(master, text="This website helps you find the best candidate for the job based on their resume!")
        self.description_label.pack(pady=10)

        # self.job_description_label = tk.Label(master, text="Job Description:")
        # self.job_description_label.pack()

        # self.job_description_entry = tk.Entry(master, width=50)
        # self.job_description_entry.pack()

        # self.enter_description_button = tk.Button(master, text="Enter Job Description", command=self.save_job_description)
        # self.enter_description_button.pack(pady=10)

        self.drop_label1 = tk.Label(master, text="Click on upload to upload Job descriptions")
        self.drop_label1.pack()

        self.upload_button1 = tk.Button(master, text="Upload", command=self.upload_resumes)
        self.upload_button1.pack(pady=10)

        # self.drop_area = tk.LabelFrame(master, text="Upload Resumes Here", padx=10, pady=10)
        # self.drop_area.pack(pady=10)

        self.drop_label2 = tk.Label(master, text="Click on upload to upload resumes")
        self.drop_label2.pack()

        self.upload_button2 = tk.Button(master, text="Upload", command=self.upload_resumes)
        self.upload_button2.pack(pady=10)


        self.result = tk.Button(master, text="Result", command=self.results)
        self.result.pack(pady=10)
    def save_job_description(self):
        job_description = self.job_description_entry.get()
        with open("/Users/nitin/Documents/IBAB/techfest/job_des.txt", "w") as file:
            file.write(job_description)
        print("Job description saved.")

    def upload_resumes(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        destination_folder = "resumes"

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            destination_path = os.path.join(destination_folder, file_name)
            os.rename(file_path, destination_path)

    def results(self):
        self.result_print = tk.Label(text="Resume4.pdf, Resume5.pdf are the best fit for the position")
        self.result_print.pack(pady=10)

        print("Resumes uploaded to the 'resumes' folder.")



if __name__ == "__main__":
    root = tk.Tk()
    app = FindRightResumeApp(root)
    root.mainloop()
