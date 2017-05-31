import QtQuick 2.7
import QtQuick.Controls 1.4
import MeetingList 1.0
import QtQuick.Window 2.2

ApplicationWindow {
    visible: true
    width: Screen.width
    height: Screen.height

    Rectangle {
        id: listArea
        width: parent.width
        height: parent.width
        color: "#fffcca"


        Component {
            id: meetingDelegate
            Rectangle {
                width: listArea.width
                height: 100
                border.color: "black"
                border.width: 1
                Column {
                    anchors.centerIn: parent  
                    Text {                        
                      text: name
                      color: "red" 
                      font.styleName: "Helvetica"
                      font.weight: Font.Bold
                    }
                }
            }
        }

        ListView { 
          id: listview1
          anchors.fill: parent
          anchors.topMargin: 100
          model: meetings
          delegate: meetingDelegate          
        }
    }

}