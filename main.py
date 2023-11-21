import logging

class VirtualClassroomManager:
    """
    Manages virtual classrooms, students, and assignments.
    """

    def __init__(self):
        self.classrooms = []

    def add_classroom(self, class_name):
        """
        Creates a new virtual classroom.

        Args:
            class_name (str): The name of the classroom.
        """

        classroom = Classroom(class_name)
        self.classrooms.append(classroom)
        logging.info(f"Classroom '{class_name}' has been created.")

    def list_classrooms(self):
        """
        Displays a list of all virtual classrooms.
        """

        logging.info(f"Number of Classrooms: {len(self.classrooms)}")
        for classroom in self.classrooms:
            logging.info(f"- {classroom.name}")

    def remove_classroom(self, class_name):
        """
        Removes a virtual classroom.

        Args:
            class_name (str): The name of the classroom to remove.
        """

        for classroom in self.classrooms:
            if classroom.name == class_name:
                self.classrooms.remove(classroom)
                logging.info(f"Classroom '{class_name}' has been removed.")
                return

        logging.warning(f"Classroom '{class_name}' not found.")


class Classroom:
    """
    Represents a virtual classroom.
    """

    def __init__(self, name):
        self.name = name
        self.students = []
        self.assignments = []

    def add_student(self, student_id):
        """
        Enrolls a student in the classroom.

        Args:
            student_id (int): The ID of the student to enroll.
        """

        student = Student(student_id)
        self.students.append(student)
        logging.info(f"Student {student_id} has been enrolled in {self.name}.")

    def list_students(self):
        """
        Displays a list of all students enrolled in the classroom.
        """

        logging.info(f"Number of Students in {self.name}: {len(self.students)}")
        for student in self.students:
            logging.info(f"- {student.id}")

    def schedule_assignment(self, assignment_details):
        """
        Schedules an assignment for the classroom.

        Args:
            assignment_details (str): The details of the assignment.
        """

        assignment = Assignment(assignment_details)
        self.assignments.append(assignment)
        logging.info(f"Assignment for {self.name} has been scheduled.")

    def list_assignments(self):
        """
        Displays a list of all scheduled assignments for the classroom.
        """

        logging.info(f"Number of Assignments in {self.name}: {len(self.assignments)}")
        for assignment in self.assignments:
            logging.info(f"- {assignment.details}")

    def submit_assignment(self, student_id, assignment_details):
        """
        Marks an assignment as submitted for a specific student.

        Args:
        student_id (int): The ID of the student submitting the assignment.
        assignment_details (str): The details of the assignment.
        """
        for student in self.students:
            if str(student.id) == student_id:
                logging.info(f"Assignment submitted by Student {student.id} in {self.name}: {assignment_details}")
                return
        logging.warning(f"Student {student_id} not found in {self.name}.")




class Student:
    """
    Represents a student.
    """

    id_counter = 1

    def __init__(self, student_id):
        self.id = Student.id_counter
        Student.id_counter += 1


class Assignment:
    """
    Represents an assignment.
    """

    def __init__(self, details):
        self.details = details


def main():
    logging.basicConfig(level=logging.INFO)
    manager = VirtualClassroomManager()

    while True:
        user_input = input("Enter command: ")
        if user_input == "exit":
            break

        try:
            parts = user_input.split(maxsplit=1)
            command = parts[0]
            args = parts[1].split() if len(parts) > 1 else []
            
            if command == "add_classroom":
                manager.add_classroom(*args)
            elif command == "list_classrooms":
                manager.list_classrooms()
            elif command == "remove_classroom":
                manager.remove_classroom(*args)
            elif command == "add_student":
                classroom_name, student_id = args
                for classroom in manager.classrooms:
                    if classroom.name == classroom_name:
                        classroom.add_student(student_id)
                        break
                else:
                    logging.warning(f"Classroom '{classroom_name}' not found.")
            elif command == "list_students":
                if args:
                    classroom_name = args[0]
                    for classroom in manager.classrooms:
                        if classroom.name == classroom_name:
                            classroom.list_students()
                            break
                    else:
                        logging.warning(f"Classroom '{classroom_name}' not found.")
                else:
                    logging.warning("Missing classroom name for list_students.")
            elif command == "schedule_assignment":
                classroom_name, *assignment_details = args
                for classroom in manager.classrooms:
                    if classroom.name == classroom_name:
                        classroom.schedule_assignment(" ".join(assignment_details))
                        break
                else:
                    logging.warning(f"Classroom '{classroom_name}' not found.")
            elif command == "list_assignments":
                classroom_name = args[0]
                for classroom in manager.classrooms:
                    if classroom.name == classroom_name:
                        classroom.list_assignments()
                        break
                else:
                    logging.warning(f"Classroom '{classroom_name}' not found.")
            elif command == "submit_assignment":
                student_id, *assignment_details = args
                classroom_name = assignment_details.pop(0) if assignment_details else None
                for classroom in manager.classrooms:
                    if classroom.name == classroom_name:
                        classroom.submit_assignment(student_id, " ".join(assignment_details))
                        break
                else:
                    logging.warning(f"Classroom '{classroom_name}' not found.")
            else:
                logging.warning("Invalid command. Please try again.")
        except Exception as e:
            logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
