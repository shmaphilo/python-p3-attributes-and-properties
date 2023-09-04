#!/usr/bin/env python3


class Person:
    APPROVED_JOBS = [
        "Admin",
        "Customer Service",
        "Human Resources",
        "ITC",
        "Production",
        "Legal",
        "Finance",
        "Marketing"
    ]

    def __init__(self, name, job):
        self._name = None
        self._job = None
        self.name = name  
        self.job = job 

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (1 <= len(value) <= 25) or not isinstance(value, str):
            raise ValueError("Name must be a string between 1 and 25 characters.")
        self._name = value.title()

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value not in self.APPROVED_JOBS:
            raise ValueError("Job must be in the list of approved jobs.")
        self._job = value

    def __str__(self):
        return f"{self.name}, {self.job}"


try:
    my_person = Person("Alice Johnson", "Manager")
except ValueError as e:
    print(e)  