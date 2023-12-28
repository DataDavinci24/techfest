import tkinter as tk
from tkinter import filedialog
import os
from agent_input import user
from JD import agent
from pdfconvs import converter

class FindRightResumeApp:
    def __init__(self, master):
        self.master = master
        master.title("Find the Right Resume!")

        self.description_label = tk.Label(master, text="This website helps you find the best candidate for the job based on their resume!")
        self.description_label.pack(pady=10)

        self.job_description_label = tk.Label(master, text="Job Description PDF:")
        self.job_description_label.pack()

        self.job_description_path = tk.StringVar()

        self.select_job_description_button = tk.Button(master, text="Select Job Description", command=self.select_job_description)
        self.select_job_description_button.pack(pady=10)

        self.drop_area = tk.LabelFrame(master, text="Upload Resumes Here", padx=10, pady=10)
        self.drop_area.pack(pady=10)

        # self.drop_label = tk.Label(self.drop_area, text="Drag and drop files here or click to select files")
        # self.drop_label.pack()
        self.resume_label = tk.Label(master, text="Resumes PDF:")
        self.resume_label.pack()

        self.upload_button = tk.Button(master, text="Upload", command=self.upload_resumes)
        self.upload_button.pack(pady=10)

        self.result = tk.Button(master, text="Result", command=self.results)
        self.result.pack(pady=10)

    def select_job_description(self):
        file_paths = filedialog.askopenfilenames(filetypes=[("PDF Files", "*.pdf")])
        destination_folder = "jds"

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        for file_path in file_paths:
            file_name = os.path.basename(file_path)
            destination_path = os.path.join(destination_folder, file_name)
            os.rename(file_path, destination_path)

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
        converter()
        user.run()
        agent.run()
        self.result_print = tk.Label(text="results")
        self.result_print.pack(pady=10)


        print("Resumes uploaded to the 'resumes' folder.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FindRightResumeApp(root)
    root.mainloop()
