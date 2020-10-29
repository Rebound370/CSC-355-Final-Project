# CSC 355 - Collaborative Image Manipulation

## Requirements
This project, to my understanding, had the following primary requirements:
- User choice on which images to manipulate
- Options for manipulating the aspect ratio
- Filter two images seperately
- Generate and composite them with a mask
- Save and show the output
- Document the code well, and create a nice readme file

## Functionality
My code interfaces with the command line to accept input from the user. It asks for the filename and path of the image, then asks whether or not a second image is going to be fed into the program. Then it asks for the desired aspect ratio. It also asks for how many circles are desired in the mask. The first image is scaled to the aspect ratio, then the second image is scaled to the first image. Filters are applied, masks are generated, then the final image is composited, saved, and displayed.

## Roles
I created the imageFiltering.py file and delegated work to the rest of the group. The intention behind the imageFiltering.py file is to accept two input images, filter them, create a mask, and blend them together. I accomplished this. Austin's code is supposed to give the user choice on what image to feed it as input, and to deal with the aspect ratio stuff. Alex was supposed to weave my code together with Austin's code. Walmiki was supposed to add documentation and create the readme file.

## Failures
I have no clue if Austin's code actually works or not. He provided the code very late, on the second to last day. Alex copy/pasted my code beneath Austin's code. The two are not properly linked together. My code does not interface with Austin's code whatsoever. My image imports have been removed, but my code does not receive an image from Austin's. Walmiki added barely any lines of documentation to the code, and did not create any sort of readme file like asked. I set clear expectations, and was let down by my group members. I didn't want to have to micromanage them, but it appears that micromanaging them was the only way that things would've gotten done properly. I also didn't want to completely solo this group project. I wanted to give them a chance to prove themselves and contribute. However, since they did not, I'm going to use this opportunity to prove myself.