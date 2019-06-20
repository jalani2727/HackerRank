import unittest

def rotLeft(a, d):
    i = 0
    new_list = [num for num in range(0,len(a))]
    for num in a:
        new_list[i-d]=a[i]
        i+=1
    return new_list


class MyTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(rotLeft([33,47,70,37,8,53,13,93,71,72,51,100,60,87,97], 13), [87,97,33,47,70,37,8,53,13,93,71,72,51,100,60])



if __name__ == '__main__':
        unittest.main()