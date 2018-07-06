from rest_framework import serializers
from itertools import zip_longest
import numpy as np
from .models import User, AvailField

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

class AvailFieldSerializer(serializers.Field):
    """
    Availability (Binary) objects into days and hourblocks
    """

    weekdays = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    # converts representation to actual storable low-level value
    def to_internal_value(self, data):
        bits = []
        for day in self.weekdays:
            bits.append(data[day])

        return bytes(np.packbits(bits))

    # converts internal value to week dictionary
    def to_representation(self, value):
        # converts internal value to 7 chunks of x 24 hours (bits)
        bitchunks = grouper(np.unpackbits(bytearray(value)), 24) # 3*8=24 is timeslots/hours per day
        # ...the 7 chunks correspond to the 7 days of the week

        week = {}
        for (bytes, day) in zip(bitchunks, self.weekdays):
            avail = []
            for bit in bytes:
                avail.append(bool(bit))
            week[day] = avail
        return week

class UserSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='users:user-detail',
        lookup_field='pk'
    )

    availability = AvailFieldSerializer()


    class Meta:
        model = User
        fields = ['url', 'netid', 'email', 'full_name', 'class_year', 'availability']
