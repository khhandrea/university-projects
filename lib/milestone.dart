import 'package:flutter/material.dart';

List<dynamic> personalGoalsList = ["Run a 5K in under 30 minutes", "Drink 8 glasses of water\neveryday for a week", "Hit normal BMI"];

List<Icon> goalIcons = [
  const Icon(Icons.fitness_center_outlined, size: 50.0, color:Color(0xff156348)), 
  const Icon(Icons.apple, size: 50.0, color: Color(0xff156348)), 
  const Icon(Icons.person, size: 50.0, color: Color(0xff156348))];
List<dynamic> category = ["Fitness", "Dietary", "Personal Goal"];
String user_name = "David Kim";

class MilestonePage extends StatefulWidget {
  const MilestonePage({super.key});
  static const routeName = '/milestone';
  @override
  State<MilestonePage> createState() => Milestone();
}

class Milestone extends State<MilestonePage> {
  bool _isDone = false;

  @override
  Widget build(BuildContext context) {
    Color getColor(Set<MaterialState> states) {
      const Set<MaterialState> interactiveStates = <MaterialState>{
        MaterialState.pressed,
        MaterialState.hovered,
        MaterialState.focused,
      };
      if (states.any(interactiveStates.contains)) {
        return Colors.blue;
      }
      return Colors.red;
    }

    // logged in user info on top
    Widget getUserInfo = Card(
      margin: const EdgeInsets.fromLTRB(15, 20, 15, 20),
      color: Colors.green,
      child: Row(
        children: [
          Container(
            margin: const EdgeInsets.all(10),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              crossAxisAlignment: CrossAxisAlignment.center,
              children: [
                CircleAvatar(
                  backgroundColor: Colors.grey[200],
                  child: const Icon(
                    Icons.person,
                    color: Colors.grey,
                  ),
                ),
              Container(
                margin: const EdgeInsets.fromLTRB(10, 0, 10, 0),
                child: Text(
                "Welcome, $user_name", 
                style: const TextStyle(
                  color: Colors.white,
                  fontWeight: FontWeight.bold,
                  fontSize: 20,
                ),
              ),
              ), 
              IconButton(
                onPressed: () => {
                  // move to profile edit

                }, 
                icon: const Icon(Icons.more_vert)
              )
              ],
            ),
          )
        ]
      ),
    );

    // Daily challenges
    Widget getDailyChallenge = Card(
      margin: const EdgeInsets.fromLTRB(15, 20, 15, 20),
      child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Container(
              margin: const EdgeInsets.all(10),
              child: Column(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(
                    "★ Daily Challenge",
                    textAlign: TextAlign.left,
                    style: TextStyle(
                      color: Colors.grey[500],
                    ),
                  ),
                  const Text("Run or walk for 30 minutes",
                    style: TextStyle(
                      color: Color(0xff88CA5E), 
                      fontSize: 20, 
                    )
                  )
                ],
              ),
            ),
          ]
        ),
      );

    Widget personalGoal = Card(
      elevation: 0,
      color: Colors.lightGreenAccent,
      child: Row(
        children: [
          const Icon(
            Icons.fitness_center, 
            size: 40,
          ),
          Checkbox(
            checkColor: Colors.blue,
            fillColor: MaterialStateProperty.resolveWith(getColor),
            value: _isDone, 
            onChanged: (value) {
              setState(() {
                _isDone = value!;
              });
            }, 
            shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
          ),
        ],
      ),
    );

    // Personal challenges
    Widget getPersonalChallenge = Card(
      margin: const EdgeInsets.fromLTRB(15, 20, 15, 20),
      child: Column(
        mainAxisAlignment: MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.stretch, 
        children: [
          Container(
            margin: const EdgeInsets.all(10),
            child: const Text(
              "Try to achieve all of your goals. You've got this!", 
              style: TextStyle(
                fontSize: 13,
                fontWeight: FontWeight.bold
              ),
            ),
          ),
          for(num i = 0; i < personalGoalsList.length; i++)
            Card(
              margin: const EdgeInsets.fromLTRB(10, 5, 10, 5),
              elevation: 0,
              color: const Color(0xffE9FFEB),
              child: Row(
                mainAxisAlignment: MainAxisAlignment.start,
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  goalIcons[i.toInt()],
                  Checkbox(
                    value: _isDone, 
                    onChanged: (value) {
                      
                    }, 
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(15)
                    ),
                  ),
                  Column(
                    mainAxisAlignment: MainAxisAlignment.start,
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        category[i.toInt()], 
                        style: const TextStyle(
                          fontSize: 20, 
                          color: Color(0xff88CA5E), 
                          height: 1.2
                        ),
                      ),
                      Text(
                        personalGoalsList[i.toInt()],
                        softWrap: true,
                      ),
                    ],
                  ),
                ],
              ),
            ),
        ]
      ),
    );

    return Scaffold(
      body: Container(
        decoration: const BoxDecoration(
          gradient: LinearGradient(
            colors: [Colors.green, Colors.white], 
            begin: Alignment.topCenter, 
            end: Alignment.bottomCenter,  
          ),
        ),
        child: Column(
          children: <Widget>[
            getUserInfo,
            getDailyChallenge,
            getPersonalChallenge, 
            // navigation bar 
          ],
        ),
      ),
    );
  }
}
