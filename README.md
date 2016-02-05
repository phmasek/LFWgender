LFWgender
=========

Getting the known gender based on name of each image in the [**Labeled Faces in the Wild**](http://vis-www.cs.umass.edu/lfw/) dataset.

This is a python script that calls the genderize.io API with the first name of the person in the image. If the confidence is more than 90% the file gets copied to the corresponding gender folder: male/female.
The image is ignored if the name is not found in the genderize.io database.


Usage
=========

 1. Change the `rootdir` variable to the directory of the **Labeled
    Faces in the Wild** dataset.
 2. Change the `maleFolder` and `femaleFolder` variables to the directory where the images should be copied based on their gender



This script was developed and used together with Labeled Faces in the Wild for the research paper found [here](https://gupea.ub.gu.se/handle/2077/38856).
