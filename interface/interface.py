from environment import b0RemoteApi

with b0RemoteApi.RemoteApiClient('b0RemoteApi_V-REP', 'b0RemoteApi', 60) as client:
    def callb(msg):
        print(msg)

    #远程调用脚本函数
    # args = [1, -1, -1, 1]
    # ret = client.simxCallScriptFunction('myFunctionName@Robotnik_Summit_XL', 'sim.scripttype_childscript', args, client.simxServiceCall())
    # print(ret)

    #远程读取关节速度数据
    motorHandles1 = client.simxGetObjectHandle('joint_front_left_wheel', client.simxServiceCall())
    motorHandles2 = client.simxGetObjectHandle('joint_front_right_wheel', client.simxServiceCall())
    motorHandles3 = client.simxGetObjectHandle('joint_back_right_wheel', client.simxServiceCall())
    motorHandles4 = client.simxGetObjectHandle('joint_back_left_wheel', client.simxServiceCall())
    print(motorHandles1)
    print(motorHandles2)
    print(motorHandles3)
    print(motorHandles4)
    #远程设置关节速度数据，但只读无法设置
    reply1 = client.simxSetObjectFloatParameter(26, 2012, 1, client.simxServiceCall())
    client.simxSetObjectFloatParameter(38, 2012, -1, client.simxServiceCall())
    client.simxSetObjectFloatParameter(32, 2012, -1, client.simxServiceCall())
    client.simxSetObjectFloatParameter(20, 2012, 1, client.simxServiceCall())
    print(reply1)
    #远程读取关节速度
    velocity = client.simxGetObjectFloatParameter(26, 2012, client.simxServiceCall())
    print(velocity)

    # #远程读取相机参数
    # vision = client.simxGetObjectHandle('Vision_sensor', client.simxServiceCall())
    # print(vision)
    # Near_clipping_plane = client.simxGetObjectFloatParameter(43, 1000, client.simxServiceCall())
    # Far_clipping_plane = client.simxGetObjectFloatParameter(43, 1001, client.simxServiceCall())
    # Perspective_angle = client.simxGetObjectFloatParameter(43, 1004, client.simxServiceCall())
    # Ortho_size = client.simxGetObjectFloatParameter(43, 1005, client.simxServiceCall())
    # print(Near_clipping_plane)
    # print(Far_clipping_plane)
    # print(Perspective_angle)
    # print(Ortho_size)
    # ResolutionX = client.simxGetObjectIntParameter(43, 1002, client.simxServiceCall())
    # ResolutionY = client.simxGetObjectIntParameter(43, 1003, client.simxServiceCall())
    # print(ResolutionX)
    # print(ResolutionY)
    # #远程设置相机参数
    # client.simxSetObjectFloatParameter(43, 1000, 0.44, client.simxServiceCall())
    # client.simxSetObjectFloatParameter(43, 1001, 0.72, client.simxServiceCall())
    # client.simxSetObjectFloatParameter(43, 1005, 88, client.simxServiceCall())
    # client.simxSetObjectIntParameter(43, 1002, 4, client.simxServiceCall())
    # client.simxSetObjectIntParameter(43, 1003, 16, client.simxServiceCall())