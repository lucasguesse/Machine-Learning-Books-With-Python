import math


class Array1D:

    def __init__(self, data):
        self.data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        if not isinstance(value, list):
            raise TypeError('data must be of type list')
        for d in value:
            if not type(d) in (int, float, bool):
                raise TypeError('all elements must be int, float or bool')
        self._data = value

    def __repr__(self):
        return 'Array1D(' + repr(self.data) + ')'

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __getitem__(self, index):
        if type(index) == int:
            return self.data[index]
        elif type(index) == list:
            new_data = [self.data[idx] for idx in index]
        elif type(index) == slice:
            new_data = self.data[index]
        else:
            raise TypeError('Must pass an int, list of ints or slice')
        return Array1D(new_data)

    def __setitem__(self, index, value):
        if type(value) in (int, float):
            if type(index) == int:
                self.data[index] = value
            elif type(index) == list:
                for idx in index:
                    self.data[idx] = value
            elif type(index) == slice:
                slice_len = len(self[index])
                if slice_len > 0:
                    self.data[index] = [value] * slice_len
            else:
                raise TypeError('Index must be an int, list of ints or slice')
        elif type(value) == list:
            if type(index) == int:
                if len(value) == 1:
                    self.data[index] = value[0]
            elif type(index) == list:
                get_len = len(self[index])
                set_len = len(value)
                if get_len == set_len:
                    for idx, val in zip(index, value):
                        self.data[idx] = val
                else:
                    raise ValueError('Incorrect dimensions: {} vs {}'
                                     .format(get_len, set_len))
            elif type(index) == slice:
                slice_len = len(self[index])
                if slice_len > 0:
                    if len(value) == 1:
                        self.data[index] = value * slice_len
                    elif len(value) == slice_len:
                        self.data[index] = value
                    else:
                        raise ValueError('Incorrect dimensions: {} vs {}'
                                         .format(slice_len, len(value)))
            else:
                raise TypeError('Index must be an int, list of ints or slice')
        elif type(value) == str:
            raise NotImplementedError('No string data yet')
        else:
            raise TypeError('Must with a numeric or list of numerics')

    def _getitem_list(self, index_list):
        return [self.data[idx] for idx in index_list]

    def _getitem_slice(self, index_slice):
        return self.data[index_slice]

    def op(self, other, op_string):
        def do_eval(d, op_string, o):
            eval_string = '{} .{}({})'
            num = eval(eval_string.format(d, op_string, o))
            if num == NotImplemented:
                d = float(d)
                num = eval(eval_string.format(d, op_string, o))
                if num == NotImplemented:
                    o = float(o)
                    num = eval(eval_string.format(d, op_string, o))
            return num

        if type(other) in (int, float):
            return Array1D([do_eval(d, op_string, other) for d in self.data])
        elif type(other) == Array1D:
            if len(self) != len(other):
                raise ValueError('Incorrect dimensions: {} vs {}'
                                 .format(len(self), len(other)))
            return Array1D([do_eval(d, op_string, other)
                            for d, o in zip(self.data, other.data)])
        else:
            raise TypeError('other must be int, float or Array1D')

    def __add__(self, other):
        return self.op(other, '__add__')

    __radd__ = __add__

    def __mul__(self, other):
        return self.op(other, '__mul__')

    __rmul__ = __mul__

    def __sub__(self, other):
        return self.op(other, '__sub__')

    def __rsub__(self, other):
        return self.op(other, '__rsub__')

    def __truediv__(self, other):
        return self.op(other, '__truediv__')

    def __rtruediv__(self, other):
        return self.op(other, '__rtruediv__')

    def __pow__(self, other):
        return self.op(other, '__pow__')

    def __rpow__(self, other):
        return self.op(other, '__rpow__')

    def __floordiv__(self, other):
        return self.op(other, '__floordiv__')

    def __rfloordiv__(self, other):
        return self.op(other, '__rfloordiv__')

    def __mod__(self, other):
        return self.op(other, '__mod__')

    def __rmod__(self, other):
        return self.op(other, '__rmod__')

    def __gt__(self, other):
        return self.op(other, '__gt__')

    def __ge__(self, other):
        return self.op(other, '__ge__')

    def __lt__(self, other):
        return self.op(other, '__lt__')

    def __le__(self, other):
        return self.op(other, '__le__')

    def __eq__(self, other):
        return self.op(other, '__eq__')

    def __ne__(self, other):
        return self.op(other, '__ne__')

    def __neg__(self):
        return Array1D([-d for d in self.data])

    def __bool__(self):
        raise ValueError(': The truth value of an array with more than '
                         'one element is ambiguous. '
                         'Use a.any() or a.all()')

    def dot(self, other):
        return sum(self * other)

    __matmul__ = dot

    def magnitude(self):
        return math.sqrt(self.dot(self))

    def dist(self, other):
        return (self - other).magnitude()

    def mean(self):
        return sum(self) / len(self)

    def max(self):
        return max(self)

    def min(self):
        return min(self)

    def sum(self):
        return sum(self)

    def prod(self):
        value = 1
        for d in self.data:
            value *= d
        return value

    def median(self):
        s = sorted(self.data)
        n = len(self)
        if n % 2:
            return s[n // 2]
        else:
            return (s[n // 2] + s[n // 2 - 1]) / 2

    def abs(self):
        return Array1D([abs(d) for d in self.data])

    __abs__ = abs

    def cumsum(self):
        cur = 0
        new_data = []
        for d in self.data:
            cur += d
            new_data.append(cur)
        return Array1D(new_data)

    def cumprod(self):
        cur = 1
        new_data = []
        for d in self.data:
            cur *= d
            new_data.append(cur)
        return Array1D(new_data)

    def argmax(self):
        idx_max = 0
        cur_max = self[0]
        for i, d in enumerate(self.data):
            if d > cur_max:
                cur_max = d
                idx_max = i
        return idx_max

    def argmin(self):
        idx_min = 0
        cur_min = self[0]
        for i, d in enumerate(self.data):
            if d < cur_min:
                cur_min = d
                idx_min = i
        return idx_min

    def round(self, decimals=0):
        return Array1D([round(d, decimals) for d in self.data])

    __round__ = round

    def all(self):
        return all(self)

    def any(self):
        return any(self)

    def var(self):
        mean = self.mean()
        return sum([abs(mean - d) ** 2 for d in self.data]) / len(self.data)

    def std(self):
        return math.sqrt(self.var())

    def cov(self, other):
        return sum((self - self.mean()) * (other - other.mean()))

    def corr(self, other):
        return self.cov(other) / (self.std() * other.std() * len(self))
