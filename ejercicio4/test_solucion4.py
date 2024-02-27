import unittest
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd

class TestModel(unittest.TestCase):

    def test_model(self):
        model = Sequential()
        model.add(Dense(32, input_shape=(3,), activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(3, activation='softmax'))

        self.assertEqual(len(model.layers), 3)
        self.assertEqual(model.layers[0].output_shape, (None, 32))
        self.assertEqual(model.layers[1].output_shape, (None, 32))
        self.assertEqual(model.layers[-1].output_shape, (None, 3))
    
    def test_modelCompilation(self):
        model = Sequential()
        model.add(Dense(32, input_shape=(3,), activation='relu'))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(3, activation='softmax'))
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    
    def test_dataPipeline(self):
        agg_data = pd.read_csv('ejercicio4/agg_data.csv')
        X_train = agg_data[['freq', 'avg_amount', 'max_amount', 'min_amount']]
        categories = agg_data['category'].unique()

        self.assertEqual(X_train.shape[1], 4)
        self.assertEqual(len(categories), 3)

if __name__ == '__main__':
    # logs = open("output.txt", "w")
    unittest.main(verbosity=2)
    # runner = unittest.TextTestRunner(logs, verbosity=2)
    # unittest.main(testRunner=runner)  






