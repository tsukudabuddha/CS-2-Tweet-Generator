#!python

from linkedlist import LinkedList
from linkedlist import Node


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = []
        for bucket in self.buckets:
            all_values.append(bucket.items)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n) Depends on the number of entries in the hashtable"""
        length = 0
        # Loop through all buckets
        for bucket in self.buckets:
            # Count number of key-value entries in each bucket
            length += bucket.length()
        return length

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Find bucket where given key belongs
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        # Check if key-value entry exists in bucket
        if bucket.find(lambda key_value: key_value[0] == key):
            return True
        return Flase

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        found_value = bucket.find(lambda key_value: key_value[0] == key)[1]

        if found_value:
            return found_value
        raise KeyError("Key not longer exists in this hash table")

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(n) Depends on length of linked_list."""
        bucket_index = self._bucket_index(key)  # Constant Time
        bucket = self.buckets[bucket_index]  # Constant Time
        if self.contains(key):
            bucket.delete(key)
        bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(n) depends on the length of the linkedlist"""
        # Find bucket where given key belongs
        bucket_index = self._bucket_index(key)  # Constant Time
        bucket = self.buckets[bucket_index]  # Constant Time
        # Check if key-value entry exists in bucket
        entry = bucket.find(lambda key_value: key_value[0] == key)
        if entry:
            # If found, delete entry associated with given key
            bucket.delete(entry)
        else:
            # Otherwise, raise error to tell user delete failed
            raise KeyError('Key not found: {}'.format(key))


def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
