﻿from pyVideoSDK import VideoSDK

class Methods:
    def __init__(self, videosdk: VideoSDK):
        self.videosdk = videosdk

    def __del__(self):
        pass

    def call(self, peerId: str) -> None:
        """Make p2p call
        
        Parameters
        ----------
        peerId : str
            A unique user ID (TrueConfID)
        """
        command = {"method": "call", "peerId": peerId}
        self.videosdk.command(command)

    def accept(self):
        """Accept the call. The command is run immediately and the result of execution is received at once.
        
        Response example
        ----------
        {"event" : "commandExecution", "accept" : "ok"}

        """
        command = {"method": "accept"}
        self.videosdk.command(command)

    def hangUp(self, forAll: bool = False):
        """End a call or a conference. The command is used when the conference has already been created. 
        hangUp() format is used during a video call. During group conferences both formats are used. 
        By using hangUp(False) format, you leave the conference, but other participants remain in the conference. 
        By using hangUp(True) the conference ends for all the participants. 
        hangUp(True) is used only if you are the conference owner, otherwise a failure occurs. 
        Positive response ("ok") means the command has been accepted for execution but has not been run executed yet. 
        Execution result will be received separately via notification.
        
        Parameters
        ----------
            forAll: bool
                True - conference ends for all the participants;                 
                False - you leave the conference, but other participants remain in the conference.
        """
        command = {"method": "hangUp", "forAll": forAll}
        self.videosdk.command(command)

    def login(self, callId: str, password: str):
        """Login to TrueConf Server"""
        command = {"method" : "login",
            "login" : callId,
            "password" : password,
            "encryptPassword" : True}
        self.videosdk.command(command)

    def logout(self):
        """Log out the current user"""
        command = {"method": "logout"}
        self.videosdk.command(command)

    def connectToServer(self, server: str, port: int = 4307):
        """Connect to TrueConf Server
        
        Parameters:

            server: str
                Server address. For example, IP address;
            port: int
                Port. Default port is 4307.
        """
        command = {"method": "connectToServer", "server": server, "port": port}
        self.videosdk.command(command)

    def sendCommand(self, peerId: str, command: str):
        command = {"method": "sendCommand", "peerId": peerId, "command": command}
        self.videosdk.command(command)

    def showMainWindow(self, maximized: bool, stayOnTop: bool = True):
        # state:
        #   1 = minimized;
        #   2 = full screen mode.        
        state = 1 if not maximized else 2
        command = {"method": "changeWindowState", "windowState": state, "stayOnTop": stayOnTop}
        self.videosdk.command(command)

    def reject(self):
        '''
        The command allows to reject incoming call or invitation to the conference
        '''
        command = {"method": "reject"}
        self.videosdk.command(command)

    def rejectPeer(self, peerId: str):
        '''
        Reject user’s request to join your conference

        Parameters:

            peerId: str 
                unique user ID
        '''
        command = {"method": "rejectPeer", "peerId": peerId}
        self.videosdk.command(command)

    def acceptPeer(self, peerId: str):
        '''
        Accept a request from the user to participate in your conference

        Parameters:

            peerId: str 
                unique user ID
        '''
        command = {"method": "acceptPeer", "peerId": peerId}
        self.videosdk.command(command)

    def createConference(self, title: str, confType: str, autoAccept: bool, inviteList: list = None):
        '''
        Create a conference with specified parameters and participants

        Parameters:

            title: str
                Title

            confType: str
                Conference type.

                Must be follow values:

                        "symmetric" - symmetric

                        "asymmetric" - assymetric

                        "role" - role-based

            autoAccept: bool
                An indicator which gives permission to automatically accept participants into the conference

            inviteList: list
                List of strings with unique user identifiers (TrueConf ID) to whom an invitation to the conference will be sent
        '''
        if inviteList:
            command = {"method": "createConference", "title": title, "confType": confType, "autoAccept": autoAccept,  "inviteList": inviteList}
        else:
            command = {"method": "createConference", "title": title, "confType": confType, "autoAccept": autoAccept}

        self.videosdk.command(command)

    def getHardware(self):
        '''
        Requesting the list of hardware.
        '''
        command = {"method" : "getHardware"}
        self.videosdk.command(command)

    def acceptFile(self, id: int):
        '''
        Accept incoming file

        Parameters:

            id: int
                request ID
        '''
        command = {"method": "acceptFile", "id": id}
        self.videosdk.command(command)

    def acceptInvitationToPodium(self):
        '''
        Accept an incoming request to the podium
        '''
        command = {"method": "acceptInvitationToPodium"}
        self.videosdk.command(command)

    def acceptRequestCameraControl(self, callId: str):
        '''
        Allow remote camera control

        Parameters:

            callId: str
                User ID (TrueConf ID)
        '''
        command = {"method": "acceptRequestCameraControl", "callId": callId}
        self.videosdk.command(command)

    def acceptRequestToPodium(self, peerId: str):
        '''
        Allow the user to enter the podium

        Parameters:

            peerId: str
                User ID (TrueConf ID)
        '''
        command = {"method": "acceptRequestToPodium", "peerId": peerId}
        self.videosdk.command(command)

    def activateLicense(self, key: str):
        '''
        Activate license key

        Parameters:

            key: str

        Example::

            sdk.activateLicense("G3K3-E929-837P-BHNQ-GKAV-GSLH-T5YU-3TJ8-ECWD-YBRV-J7A2")
        '''
        command = {"method": "activateLicense", "key": key}
        self.videosdk.command(command)

    def addSlide(self, fileId: int):
        '''
        Add a new slide to SlideShow

        Parameters:

            fileId: int

                File ID in http-server
        '''
        command = {"method": "addSlide", "fileId": fileId}
        self.videosdk.command(command)

    def addToAbook(self, peerId: str, peerDn: str):
        '''
        Add a user to address book

        Parameters:

            peerId: str
                User ID (TrueConf ID)

            peerDn: str
                Display name
        '''
        command = {"method": "addToAbook", "peerId" : peerId, "peerDn": peerDn}
        self.videosdk.command(command)

    def addToGroup(self, groupId: int, peerId: str):
        '''
        Add the user to a group in the address book

        Parameters:

            groupId: int
              Group ID

            peerId: str
                User ID (TrueConf ID)
        '''
        command = {"method": "addToGroup", "groupId": groupId, "peerId": peerId}
        self.videosdk.command(command)

    def allowRecord(self, peerId: str):
        '''
        Allow video recording for a user

        Parameters:

            peerId: str
                User ID (TrueConf ID)
        '''
        command = {"method": "allowRecord", "peerId": peerId}
        self.videosdk.command(command)

    def block(self, peerId: str):
        '''
        Add user to block list

        Parameters:

            peerId: str
                User ID (TrueConf ID)
        '''
        command = {"method": "block", "peerId": peerId}
        self.videosdk.command(command)

    def changeCurrentMonitor(self, monitorIndex: int):
        '''
        Move the main window to the specified monitor

        Parameters:

            monitorIndex: int
                The specified monitor's index
        '''
        command = {"method": "changeCurrentMonitor", "monitorIndex": monitorIndex}
        self.videosdk.command(command)

    def changeVideoMatrixType(self, matrixType: int):
        '''
        Change the current matrix (layout) type.
        '''
        command = {"method": "changeVideoMatrixType", "matrixType": matrixType}
        self.videosdk.command(command)

    def changeWindowState(self, windowState: int, stayOnTop: bool):
        '''
        Change the state of the main application window.

        Parameters:

            windowState: int
                Window state

            stayOnTop: bool

        '''
        command = {"method": "changeWindowState", "windowState": windowState, "stayOnTop": stayOnTop}
        self.videosdk.command(command)

    def chatClear(self, id: str):
        '''
        Clear a user's chat history

        Parameters:

            id: str
                User ID (TrueConf ID)
        '''
        command = {"method": "chatClear", "id": id}
        self.videosdk.command(command)

    def clearCallHistory(self):
        '''
        Clear call history
        '''
        command = {"method": "clearCallHistory"}
        self.videosdk.command(command)

    def clearFileTransfer(self):
        '''
        Clear file sharing history and delete files
        '''
        command = {"method": "clearFileTransfer"}
        self.videosdk.command(command)

    def clearTokens(self):
        '''
        Clear all tokens
        '''
        command = {"method": "clearTokens"}
        self.videosdk.command(command)

    def connectToService(self):
        '''
        Connect to trueconf.com service
        '''
        command = {"method": "connectToService"}
        self.videosdk.command(command)

    def createGroup(self, name: str):
        '''
        Create a users group in address book
        '''
        command = {"method": "createGroup", "name": name}
        self.videosdk.command(command)

    def createNDIDevice(self, deviceId: str):
        '''
        Create an NDI source from a conference participant

        Parameters:

            deviceId: str
                User ID (TrueConf ID)

        Example::

            sdk.createNDIDevice("user1@some.server")
        '''
        command = {"method": "createNDIDevice", "deviceId": deviceId}
        self.videosdk.command(command)

    def deleteData(self, containerName: str):
        '''
        Delete a data container

        Parameters:

            containerName: str
                Container name
        '''
        command = {"method": "deleteData", "containerName": containerName}
        self.videosdk.command(command)

    def deleteFileTransferFile(self, fileId: int):
        '''
        Delete a file from the file sharing history

        Parameters:

            fileId: int
                File ID
        '''
        command = {"method": "deleteFileTransferFile", "fileId": fileId}
        self.videosdk.command(command)

    def deleteNDIDevice(self, deviceId: str):
        '''
        Delete NDI source

        Parameters:

            deviceId: str
                User ID (TrueConf ID)

        Example::

            sdk.deleteNDIDevice("user1@some.server")
        '''
        command = {"method": "deleteNDIDevice", "deviceId": deviceId}
        self.videosdk.command(command)

    def denyRecord(self, peerId: str):
        '''
        Deny recording audio stream and video stream

        Parameters:

            peerId: str
                User ID (TrueConf ID)
        '''
        command = {"method": "denyRecord", "peerId": peerId}
        self.videosdk.command(command)

    def enableAudioReceiving(self, peerId: str, enable: bool):
        '''
        Enable or disable audio receiving from user - "peerId"

        Parameters:

            peerId: str
                User ID (TrueConf ID)

            enable: bool
        '''
        command = {"method": "enableAudioReceiving", "peerId": peerId, "enable": enable}
        self.videosdk.command(command)

    def enableVideoReceiving(self, peerId: str, enable: bool):
        '''
        Enable or disable video receiving from user - "peerId"

        Parameters:

            peerId: str
                User ID (TrueConf ID)

            enable: bool
        
        Example::

            # Switching video off from user "user1@some.server"
            sdk.enableVideoReceiving("user1@some.server", False)
        '''
        command = {"method": "enableVideoReceiving", "peerId": peerId, "enable": enable}
        self.videosdk.command(command)

    def expandCallToMulti(self, title: str, inviteList: list):
        '''
        Transform the current videocall to a group conference

        Parameters:

            title: str
                Conference title

            inviteList: list
                Invited list
        
        Example::

            sdk.expandCallToMulti(title="New group conference", inviteList=["user1@some.server", "user2@some.server", "user3@some.server"])
        '''
        command = {"method": "expandCallToMulti", "title": title, "inviteList": inviteList}
        self.videosdk.command(command)

    def fireMyEvent(self, data: str):
        '''
        Fire a custom event

        Parameters:

            data: str
                Any data string

        Example::

             sdk.fireMyEvent("power off")
        '''
        command = {"method": "fireMyEvent", "data": data}
        self.videosdk.command(command)

    def getAbook(self):
        '''
        Request the address book
        '''
        command = {"method": "getAbook"}
        self.videosdk.command(command)

    def getAllUserContainersNames(self):
        '''
        Request names of all data containers
        '''
        command = {"method": "getAllUserContainersNames"}
        self.videosdk.command(command)

    def getAppSndDev(self):
        '''
        Request information about the current sound playback device
        '''
        command = {"method": "getAppSndDev"}
        self.videosdk.command(command)

    def getAppState(self):
        '''
        Request the application state
        '''
        command = {"method": "getAppState"}
        self.videosdk.command(command)

    def getAudioDelayDetectorInfo(self):
        '''
        Get an echo test information
        '''
        command = {"method": "getAudioDelayDetectorInfo"}
        self.videosdk.command(command)

    def getAudioMute(self):
        '''
        Get audio state
        '''
        command = {"method": "getAudioMute"}
        self.videosdk.command(command)

    def getAudioReceivingLevel(self, peerId: str):
        '''
        Get the current volume level of the conference participant

        Parameters:

            peerId: str
                User ID (TrueConf ID)
        '''
        command = {"method": "getAudioReceivingLevel", "peerId": peerId}
        self.videosdk.command(command)

    def getAuthInfo(self):
        '''
        Get information about the type of protection for the administrator and user accounts
        '''
        command = {"method": "getAuthInfo"}
        self.videosdk.command(command)

    def getAvailableServersList(self):
        command = {"method": "getAvailableServersList"}
        self.videosdk.command(command)

    def getBackground(self):
        command = {"method": "getBackground"}
        self.videosdk.command(command)

    def getBanList(self):
        '''
        Get the list of blocked users
        '''
        command = {"method": "getBanList"}
        self.videosdk.command(command)

    def getBroadcastPicture(self):
        '''
        Get the name of the file containing the picture that can be broadcasted instead of your own video
        '''
        command = {"method": "getBroadcastPicture"}
        self.videosdk.command(command)

    def getBroadcastSelfie(self):
        '''
        Get to know if you can view the video using current camera
        '''
        command = {"method": "getBroadcastSelfie"}
        self.videosdk.command(command)

    def getCallHistory(self, count: int):
        '''
        Get a list of recent calls

        Parameters:

            count: int
                Amount of requested calls

        Example::

            sdk.getCallHistory(10)
        '''
        command = {"method": "getCallHistory", "count": count}
        self.videosdk.command(command)

    def getChatLastMessages(self, id: str, beginNumber: int, count: int):
        command = {"method": "getChatLastMessages", "id": id, "beginNumber": beginNumber, "count": count}
        self.videosdk.command(command)

    def getConferenceParticipants(self):
        '''
        To view conference participants list
        '''
        command = {"method": "getConferenceParticipants"}
        self.videosdk.command(command)

    def getConferences(self):
        command = {"method": "getConferences"}
        self.videosdk.command(command)

    def getConnected(self):
        command = {"method": "getConnected"}
        self.videosdk.command(command)

    def getContactDetails(self, peerId: str):
        '''
        Get contact’s personal details

        Parameters:

            peerId: str
                User ID (TrueConf ID)

        Example::

            sdk.getContactDetails("user1@some.server")
        '''
        command = {"method": "getContactDetails", "peerId": peerId}
        self.videosdk.command(command)

    def getCreatedNDIDevices(self):
        command = {"method": "getCreatedNDIDevices"}
        self.videosdk.command(command)

    def getCrop(self):
        command = {"method": "getCrop"}
        self.videosdk.command(command)

    def getCurrentUserProfileUrl(self):
        command = {"method": "getCurrentUserProfileUrl"}
        self.videosdk.command(command)

    def getDisplayNameById(self, peerId: str):
        '''
        Get display name using user ID

        Parameters:

            peerId: str
                User ID (TrueConf ID)

        Example::

            sdk.getDisplayNameById("user1@some.server")
        '''
        command = {"method": "getDisplayNameById", "peerId": peerId}
        self.videosdk.command(command)

    def getFileInfo(self, id: int):
        command = {"method": "getFileInfo", "id": id}
        self.videosdk.command(command)

    def getFileList(self):
        '''
        Get the list of URLs of downloaded files
        '''
        command = {"method": "getFileList"}
        self.videosdk.command(command)

    def getFileRequests(self):
        '''
        Get the list of incoming files
        '''
        command = {"method": "getFileRequests"}
        self.videosdk.command(command)

    def getFileTransferAvailability(self):
        '''
        Get file transfer availability
        '''
        command = {"method": "getFileTransferAvailability"}
        self.videosdk.command(command)

    def getFileTransferInfo(self):
        '''
        Get file transfer information
        '''
        command = {"method": "getFileTransferInfo"}
        self.videosdk.command(command)

    def getFileUploads(self):
        '''
        Get the list of outgoing files
        '''
        command = {"method": "getFileUploads"}
        self.videosdk.command(command)

    def getGroups(self):
        '''
        Get information about groups
        '''
        command = {"method": "getGroups"}
        self.videosdk.command(command)

    def getHardwareKey(self):
        '''
        Get a unique hardware key to create a license
        '''
        command = {"method": "getHardwareKey"}
        self.videosdk.command(command)

    def getHttpServerSettings(self):
        '''
        Get http server settings
        '''
        command = {"method": "getHttpServerSettings"}
        self.videosdk.command(command)

    def getHttpServerState(self):
        '''
        Get http server status
        '''
        command = {"method": "getHttpServerState"}
        self.videosdk.command(command)
