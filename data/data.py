import sys

PAGE_POS = 2
PER_PAGE = 6
PAGE_NEG = ("", '%', " ", 6.6, -2, "Ошибка", "John", sys.maxsize, "<script>alert(123)</script>")
NAME_POS = ("Jack", "Джек", "Rick Role")
JOB_POS = ("QA", "Писатель", "QA engineer")
NAME_AND_JOB_NEG = ("", '$', " ", 8.9, 6, " *Jack. ", "<script>alert(123)</script>")
