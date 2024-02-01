freqs = {"la": 220,
         "si": 247,
         "do": 261,
         "re": 293,
         "mi": 329,
         "fa": 349,
         "sol": 392,
         }


notes = "sol,250-mi,250-mi,500-fa,250-re,250-re,500-do,250-re,250-mi,250-fa,250-sol,250-sol,250-sol,500"

import winsound

notes = notes.split("-")
for note in notes:
    note = note.split(",")
    winsound.Beep(freqs[note[0]], int(note[1]))


numbers = iter(list(range(1, 101)[:-1:]))
for i in numbers:
    print(i)
    next(numbers)
    next(numbers)


from itertools import combinations
arr = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
def rSubset(arr, r):

    return list(combinations(arr, r))
comb = []
count = 0
for i in range(7, len(arr)+1):
    iter_sub = rSubset(arr,i)
    for sub in iter_sub:
        if sum(sub) == 100:
            comb.append(sub)

print(len(set(comb)))

class MusicNotes:
    def __init__(self):
        self._notes_lst = []
        self.note_index = -1
        notes_table = [55, 61.74, 65.41, 73.42, 82.41, 87.31, 98]
        for i in range(1, 6):
            for j in range(len(notes_table)):
                self.add_note(notes_table[j])
                notes_table[j] *= 2


    def add_note(self, new_note):
        self._notes_lst.append(new_note)

    def __iter__(self):
        return self

    def __next__(self):
        if self.note_index >= len(self._notes_lst) - 1:
            raise StopIteration()
        self.note_index += 1
        return self._notes_lst[self.note_index]


notes_iter = iter(MusicNotes())
for freq in notes_iter:
    print(freq)

def check_id_valid(id_number):
    if len(id_number) != 9:
        return False
    sum1 = 0

    for i in range(9):
        if i % 2 == 0:
            sum1 += int(id_number[i])
        else:
            dig = 2 * int(id_number[i])
            if dig > 9:
                dig = (dig % 10) + (dig//10)
            sum1 += dig
    if sum1 % 10 == 0:
        return True
    return False

print(check_id_valid("123456780"))
print(check_id_valid("123456782"))


class IDIterator:
    def __init__(self,id):
        self.__id = id

    def __iter__(self):
        return self.__id

    def __next__(self):
        next_id = int(self.__id) + 1
        while not check_id_valid(str(next_id)):
            next_id += 1
        if next_id > 999999999:
            raise StopIteration()
        return str(next_id)

def main():
    id = input("Enter ID")
    id_iter = IDIterator(id)
    for i in range(10):
        for j in id_iter:
            print(j)


main()