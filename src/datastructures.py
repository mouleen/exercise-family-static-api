
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id=1
        # example list of members
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jane",
                "last_name": last_name,
                "age": 35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id": self._generate_id(),
                "first_name": "Jimmy",
                "last_name": last_name,
                "age": 5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id +=1
        return generated_id

    def add_member(self, member):
        # fill this method and update the return
        member['id'] = self._generate_id()
        self._members.append(member)

        return list(self._members)

    def delete_member(self, id):
        # fill this method and update the return
        # if self.get_member(id):
        self._members=list(filter(lambda x: x["id"] != id, self._members))
        return list(self._members)

    def get_member(self, id): 
        return list(filter(lambda x: x["id"] == id, self._members))
        

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return list(self._members)
