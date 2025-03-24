import maya.cmds as cm
from maya.mel import eval
import maya.OpenMaya as om
import maya.OpenMayaUI as omui

def fk_to_ik():
    sel = cm.ls(sl=True)
    name_space = sel[0].rpartition(":")[0]

    if len(sel) == 3:
        wrist_loc = cm.spaceLocator(name="wrist_loc")
        elbow_loc = cm.spaceLocator(name="elbow_loc")
        for i in sel:
            if "FKWrist" in str(i):
                cm.parentConstraint(i, wrist_loc, mo=False)
            if "FKElbow" in str(i):
                cm.parentConstraint(i, elbow_loc, mo=False)
            if "FKIKArm" in str(i):
                cm.setAttr("{}.FKIKBlend".format(i), 10)

        min_time = cm.playbackOptions(q=True, min=True)
        max_time = cm.playbackOptions(q=True, max=True)
        cm.select(wrist_loc, elbow_loc)
        eval(
            'bakeResults -simulation true -t "{0}:{1}" -sampleBy 1 -oversamplingRate 1 '
            '-disableImplicitControl true -preserveOutsideKeys true -sparseAnimCurveBake false '
            '-removeBakedAttributeFromLayer false -removeBakedAnimFromLayer false -bakeOnOverrideLayer '
            'false -minimizeRotation true -controlPoints false -shape false;'.format(
                min_time, max_time))
        if "_R" in str(sel[0]):
            cm.pointConstraint(wrist_loc, "{}:IKArm_R".format(name_space), mo=False)
            cm.orientConstraint(wrist_loc, "{}:IKArm_R".format(name_space), mo=False)
            cm.parentConstraint(elbow_loc, "{}:PoleArm_R".format(name_space), mo=False, sr=["x", "y", "z"])
            cm.select("{}:IKArm_R".format(name_space), "{}:PoleArm_R".format(name_space))
            eval(
                'bakeResults -simulation true -t "{0}:{1}" -sampleBy 1 -oversamplingRate 1 '
                '-disableImplicitControl true -preserveOutsideKeys true -sparseAnimCurveBake false '
                '-removeBakedAttributeFromLayer false -removeBakedAnimFromLayer false -bakeOnOverrideLayer '
                'false -minimizeRotation true -controlPoints false -shape false;'.format(
                    min_time, max_time))
            cm.delete(wrist_loc, elbow_loc)
        if "_L" in str(sel[0]):
            cm.pointConstraint(wrist_loc, "{}:IKArm_L".format(name_space), mo=False)
            cm.orientConstraint(wrist_loc, "{}:IKArm_L".format(name_space), mo=False)
            cm.parentConstraint(elbow_loc, "{}:PoleArm_L".format(name_space), mo=False, sr=["x", "y", "z"])
            cm.select("{}:IKArm_L".format(name_space), "{}:PoleArm_L".format(name_space))
            eval(
                'bakeResults -simulation true -t "{0}:{1}" -sampleBy 1 -oversamplingRate 1 '
                '-disableImplicitControl true -preserveOutsideKeys true -sparseAnimCurveBake false '
                '-removeBakedAttributeFromLayer false -removeBakedAnimFromLayer false -bakeOnOverrideLayer '
                'false -minimizeRotation true -controlPoints false -shape false;'.format(
                    min_time, max_time))
            cm.delete(wrist_loc, elbow_loc)
    elif len(sel) == 6:
        wrist_loc_R = cm.spaceLocator(name="wrist_loc_R")
        wrist_loc_L = cm.spaceLocator(name="wrist_loc_L")
        elbow_loc_R = cm.spaceLocator(name="elbow_loc_R")
        elbow_loc_L = cm.spaceLocator(name="elbow_loc_L")
        for i in sel:
            if "FKWrist_R" in str(i):
                cm.parentConstraint(i, wrist_loc_R, mo=False)
            if "FKElbow_R" in str(i):
                cm.parentConstraint(i, elbow_loc_R, mo=False)
            if "FKIKArm_R" in str(i):
                cm.setAttr("{}.FKIKBlend".format(i), 10)
            if "FKWrist_L" in str(i):
                cm.parentConstraint(i, wrist_loc_L, mo=False)
            if "FKElbow_L" in str(i):
                cm.parentConstraint(i, elbow_loc_L, mo=False)
            if "FKIKArm_L" in str(i):
                cm.setAttr("{}.FKIKBlend".format(i), 10)

        min_time = cm.playbackOptions(q=True, min=True)
        max_time = cm.playbackOptions(q=True, max=True)
        cm.select(wrist_loc_R, wrist_loc_L, elbow_loc_R, elbow_loc_L)
        eval(
            'bakeResults -simulation true -t "{0}:{1}" -sampleBy 1 -oversamplingRate 1 '
            '-disableImplicitControl true -preserveOutsideKeys true -sparseAnimCurveBake false '
            '-removeBakedAttributeFromLayer false -removeBakedAnimFromLayer false -bakeOnOverrideLayer '
            'false -minimizeRotation true -controlPoints false -shape false;'.format(
                min_time, max_time))
        cm.pointConstraint(wrist_loc_R, "{}:IKArm_R".format(name_space), mo=False)
        cm.orientConstraint(wrist_loc_R, "{}:IKArm_R".format(name_space), mo=False)
        cm.parentConstraint(elbow_loc_R, "{}:PoleArm_R".format(name_space), mo=False, sr=["x", "y", "z"])

        cm.pointConstraint(wrist_loc_L, "{}:IKArm_L".format(name_space), mo=False)
        cm.orientConstraint(wrist_loc_L, "{}:IKArm_L".format(name_space), mo=False)
        cm.parentConstraint(elbow_loc_L, "{}:PoleArm_L".format(name_space), mo=False, sr=["x", "y", "z"])

        cm.select("{}:IKArm_L".format(name_space), "{}:PoleArm_L".format(name_space), "{}:IKArm_R".format(name_space), "{}:PoleArm_R".format(name_space))
        eval(
            'bakeResults -simulation true -t "{0}:{1}" -sampleBy 1 -oversamplingRate 1 '
            '-disableImplicitControl true -preserveOutsideKeys true -sparseAnimCurveBake false '
            '-removeBakedAttributeFromLayer false -removeBakedAnimFromLayer false -bakeOnOverrideLayer '
            'false -minimizeRotation true -controlPoints false -shape false;'.format(
                min_time, max_time))

        cm.delete(wrist_loc_L, elbow_loc_L, wrist_loc_R, elbow_loc_R)

    elif len(sel) == 12:
        wrist_loc_R = cm.spaceLocator(name="wrist_loc_R")
        wrist_loc_L = cm.spaceLocator(name="wrist_loc_L")
        elbow_loc_R = cm.spaceLocator(name="elbow_loc_R")
        elbow_loc_L = cm.spaceLocator(name="elbow_loc_L")
        for i in sel:
            if "FKWrist_R" in str(i):
                cm.parentConstraint(i, wrist_loc_R, mo=False)
            if "FKElbow_R" in str(i):
                cm.parentConstraint(i, elbow_loc_R, mo=False)
            if "FKIKArm_R" in str(i):
                cm.setAttr("{}.FKIKBlend".format(i), 10)
            if "FKWrist_L" in str(i):
                cm.parentConstraint(i, wrist_loc_L, mo=False)
            if "FKElbow_L" in str(i):
                cm.parentConstraint(i, elbow_loc_L, mo=False)
            if "FKIKArm_L" in str(i):
                cm.setAttr("{}.FKIKBlend".format(i), 10)

        min_time = cm.playbackOptions(q=True, min=True)
        max_time = cm.playbackOptions(q=True, max=True)
        cm.select(wrist_loc_R, wrist_loc_L, elbow_loc_R, elbow_loc_L)
        eval(
            'bakeResults -simulation true -t "{0}:{1}" -sampleBy 1 -oversamplingRate 1 '
            '-disableImplicitControl true -preserveOutsideKeys true -sparseAnimCurveBake false '
            '-removeBakedAttributeFromLayer false -removeBakedAnimFromLayer false -bakeOnOverrideLayer '
            'false -minimizeRotation true -controlPoints false -shape false;'.format(
                min_time, max_time))
        cm.pointConstraint(wrist_loc_R, "{}:IKArm_R".format(name_space), mo=False)
        cm.orientConstraint(wrist_loc_R, "{}:IKArm_R".format(name_space), mo=False)
        cm.parentConstraint(elbow_loc_R, "{}:PoleArm_R".format(name_space), mo=False, sr=["x", "y", "z"])

        cm.pointConstraint(wrist_loc_L, "{}:IKArm_L".format(name_space), mo=False)
        cm.orientConstraint(wrist_loc_L, "{}:IKArm_L".format(name_space), mo=False)
        cm.parentConstraint(elbow_loc_L, "{}:PoleArm_L".format(name_space), mo=False, sr=["x", "y", "z"])

        cm.select("{}:IKArm_L".format(name_space), "{}:PoleArm_L".format(name_space), "{}:IKArm_R".format(name_space),
                  "{}:PoleArm_R".format(name_space))
        eval(
            'bakeResults -simulation true -t "{0}:{1}" -sampleBy 1 -oversamplingRate 1 '
            '-disableImplicitControl true -preserveOutsideKeys true -sparseAnimCurveBake false '
            '-removeBakedAttributeFromLayer false -removeBakedAnimFromLayer false -bakeOnOverrideLayer '
            'false -minimizeRotation true -controlPoints false -shape false;'.format(
                min_time, max_time))

        cm.delete(wrist_loc_L, elbow_loc_L, wrist_loc_R, elbow_loc_R)

    else:
        om.MGlobal_displayError("Please chose only 3 control for 1 arm or 6 control for 2 arm to process")

