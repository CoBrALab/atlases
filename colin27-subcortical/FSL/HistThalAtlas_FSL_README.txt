Questions about the atlas interacting with FSLeyes can be directed to Erin Mazerolle 
(erinmaz@gmail.com).

This atlas was modified from the one described in:
Neuroimage. 2006 Apr 1;30(2):359-76. Epub 2006 Jan 9.
The creation of a brain atlas for image guided neurosurgery using serial histological data.
Chakravarty MM, Bertrand G, Hodge CP, Sadikot AF, Collins DL.

The following steps were performed:
Atlas was converted from minc to nifti and labels were assigned the closest integer value
Calculation of warp to register Colin27 to MNI_152_1mm with FNIRT
Application of that warp to the atlas, output in 1mm and 2mm MNI space 
Generation of xml file 


INSTRUCTIONS:

Save HistThalAtlas.tar to ${FSLDIR}/data/atlases (sudo will likely be necessary).

Then, in a terminal type:
cd ${FSLDIR}/data/atlases
sudo tar -xvf HistThalAtlas.tar

"Histological Thalamus Atlas" should now be an option in FSLeyes and atlasquery. 
To access the atlas:
Open FSLeyes
Go:
File -> Add standard
Select MNI_152_1mm.nii.gz
Go:
Settings -> OrthoView 1 -> Atlas panel
Histological Thalamus Atlas should be an option under the "Atlas information" tab. Select 
it, and click the "Show/Hide" link next to its name (its name will appear in the panel 
directly to the right after you select it).
