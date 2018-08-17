from keras.layers import *
from keras.models import Sequential

def autoencoder(image_shape=(240, 240, 1), encoder_only=False, activation='relu'):
    
    # Encoder
    model = Sequential()
    model.add(Conv2D(8, (3,3), padding='same', activation=activation, input_shape=image_shape))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2,2)))
    
    model.add(Conv2D(16, (3,3), padding='same', activation=activation))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2,2)))
    
    model.add(Conv2D(32, (3,3), padding='same', activation=activation))
    model.add(BatchNormalization())
    model.add(MaxPool2D((2,2)))
    
    model.add(Conv2D(64, (3,3), padding='same', activation=activation))
    model.add(BatchNormalization())
#     model.add(MaxPool2D((2,2)))
    
    if encoder_only:
        model.add(Flatten())
        return model
    
    # Decoder
    model.add(UpSampling2D((2,2)))
    model.add(Conv2D(32, (3,3), padding='same', activation=activation))
    model.add(BatchNormalization())
    
    model.add(UpSampling2D((2,2)))
    model.add(Conv2D(16, (3,3), padding='same', activation=activation))
    model.add(BatchNormalization())
    
    model.add(UpSampling2D((2,2)))
    model.add(Conv2D(8, (3,3), padding='same', activation=activation))
    model.add(BatchNormalization())
    
    model.add(Conv2D(1, (3,3), padding='same'))   
    return model