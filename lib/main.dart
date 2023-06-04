import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'dart:math';
import 'package:intl/intl.dart';
import 'package:daily_diet_date/milestone.dart';
import 'package:daily_diet_date/sign_in.dart';
import 'package:flutter/material.dart';
import 'sign_up.dart';
import 'reward.dart';

class Challenge {
  final String category;
  final String description;

  Challenge({required this.category, required this.description});
}
final List<String> userInputList = [];
List<Challenge> weightLossChallenges = [
  Challenge(category: 'Weight Loss', description: 'Take a 30-minute brisk walk today.'),
  Challenge(category: 'Weight Loss', description: 'Replace sugary drinks with water for the entire day.'),
  Challenge(category: 'Weight Loss', description: 'Do 10 minutes of high-intensity interval training (HIIT).'),
  // Add more weight loss challenges
];

List<Challenge> healthyEatingChallenges = [
  Challenge(category: 'Healthy Eating', description: 'Eat at least five servings of fruits and vegetables today.'),
  Challenge(category: 'Healthy Eating', description: 'Cook a healthy homemade meal for dinner.'),
  Challenge(category: 'Healthy Eating', description: 'Choose whole grain options for your breakfast.'),
  // Add more healthy eating challenges
];

List<Challenge> healthyLifestyleChallenges = [
  Challenge(category: 'Healthy Lifestyle', description: 'Practice meditation or deep breathing for 10 minutes.'),
  Challenge(category: 'Healthy Lifestyle', description: 'Get at least 8 hours of quality sleep tonight.'),
  Challenge(category: 'Healthy Lifestyle', description: 'Take a break from screens and engage in a hobby or physical activity.'),
  // Add more healthy lifestyle challenges
];

Challenge getChallengeBasedOnTime(List<Challenge> challenges) {
  final DateTime now = DateTime.now();
  final int day = now.day;
  final Challenge selectedChallenge = challenges[day % challenges.length];
  return selectedChallenge;
}
void main() {
  final weightLossChallenge = getChallengeBasedOnTime(weightLossChallenges);
  final healthyEatingChallenge = getChallengeBasedOnTime(healthyEatingChallenges);
  final healthyLifestyleChallenge = getChallengeBasedOnTime(healthyLifestyleChallenges);
  // Generate challenges based on the current time of the day
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Navigation',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      routes: {
        '/': (context) => MainPage(), // Set the main page as the home
        SignInPage.routeName: (context) => SignInPage(),
        ProfilePage.routeName: (context) => ProfilePage(),
        View_ProfilePage.routeName: (context) => View_ProfilePage(userInputList: [],)
      },
    );
  }
}

class MainPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    Widget getInfoSection = Card();
    return Scaffold(
      body: Container(
        decoration: BoxDecoration(
          gradient: LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [Colors.green.shade400, Colors.white],
          ),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Image.asset(
              'assets/welcome.png',
              height: 150,
            ),
            SizedBox(height: 16),
            Image.asset(
              'assets/robot.png',
              height: 200,
            ),
            SizedBox(height: 16),
            Column(
              children: [
                SizedBox(height: 16),
                Column(
                  children: [
                    GestureDetector(
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => SignInPage(),
                          ),
                        );
                      },
                      child: SizedBox(
                        width: 300,
                        height: 50,
                        child: Image.asset(
                          'assets/login.png',
                          fit: BoxFit.cover,
                        ),
                      ),
                    ),
                    SizedBox(height: 16),
                    GestureDetector(
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => ProfilePage(),
                          ),
                        );
                      },
                      child: SizedBox(
                        width: 300,
                        height: 50,
                        child: Image.asset(
                          'assets/signup.png',
                          fit: BoxFit.cover,
                        ),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}

class SignInPage extends StatelessWidget {
  static const routeName = '/sign-in';

  @override
  Widget build(BuildContext context) {

    Widget getInfoSection = Card(
      margin: const EdgeInsets.fromLTRB(15, 0, 15, 0),
      elevation: 0,
      child: Column(
        // mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Expanded(
              flex: 1,
              child: Column(
                children: [
                  Expanded(
                    flex: 5,
                    child: CircleAvatar(
                      backgroundColor: Colors.grey[200],
                      radius: 60,
                      child: const Icon(
                        Icons.person,
                        color: Colors.grey,
                        size: 80,
                      ),
                    ),
                  ),
                  Expanded(
                      flex: 1,
                      child: Text(
                        "Please enter your details",
                        style: TextStyle(
                          color: Colors.green.shade500,
                          fontSize: 20,
                        ),
                      )
                  )
                ],
              )
          ),
          Expanded(
            flex: 2,
            child: Column(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                _personalDetailInfo("Name"),
                _personalDetailInfo("User Name"),
                _personalDetailInfo("Password"),
                _personalDetailInfo("Age"),
                _personalDetailInfo("Email"),
                _personalDataInfoButton(),
              ],
            ),
          )
        ],
      ),
    );

    return AnnotatedRegion<SystemUiOverlayStyle>(
      value: SystemUiOverlayStyle.dark,
      child: Container(
          decoration: BoxDecoration(
            gradient: LinearGradient(
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
                colors: [ Colors.white, Colors.green.shade200 ]
            ),
          ),
          child: Column(
            children: [
              Expanded(
                  flex: 2,
                  child: Container(
                      decoration: const BoxDecoration(
                          image: DecorationImage(
                              image: AssetImage('assets/robot-lookDown.png'),
                              fit: BoxFit.cover
                          )
                      )
                  )
              ),
              Expanded(
                flex: 10,
                child: Container(
                  margin: const EdgeInsets.fromLTRB(20, 0, 20, 50),
                  height: double.infinity,
                  width: double.infinity,
                  decoration: const BoxDecoration(
                      color: Colors.white,
                      borderRadius: BorderRadius.all(Radius.circular(8)),
                      boxShadow: [
                        BoxShadow(
                          color: Colors.grey,
                          spreadRadius: 1,
                          blurRadius: 3,
                          offset: Offset(0, 3),
                        )
                      ]
                  ),
                  child: getInfoSection,
                ),
              )
            ],
          )
      ),
    );
  }

  TextField _personalDetailInfo(String label) {
    return TextField(
      decoration: InputDecoration(
        enabledBorder: const OutlineInputBorder(
            borderSide: BorderSide(
              width: 1, color: Colors.lightGreen,
            ),
            borderRadius: BorderRadius.all(Radius.circular(10))
        ),
        focusedBorder: const OutlineInputBorder(
            borderSide: BorderSide(
              width: 1, color: Colors.green,
            ),
            borderRadius: BorderRadius.all(Radius.circular(10))
        ),
        labelText: label,
      ),
    );
  }

  ElevatedButton _personalDataInfoButton() {
    return ElevatedButton(
      style: ButtonStyle(
          foregroundColor: const MaterialStatePropertyAll(Colors.white),
          backgroundColor: MaterialStatePropertyAll(Colors.green.shade300),
          fixedSize: const MaterialStatePropertyAll(Size(160, 50)),
          elevation: const MaterialStatePropertyAll(3)
      ),
      onPressed: null, // TODO have to be implemented 'onPressed'
      child: const Text(
        "Sign Up",
        style: TextStyle(
            fontSize: 17,
            fontWeight: FontWeight.bold
        ),
      ),
    );
  }
}

class ProfilePage extends StatelessWidget {
  List<String> userInputList = List<String>.filled(5, '');
  final weightLossChallenge = getChallengeBasedOnTime(weightLossChallenges);
  final healthyEatingChallenge = getChallengeBasedOnTime(healthyEatingChallenges);
  final healthyLifestyleChallenge = getChallengeBasedOnTime(healthyLifestyleChallenges);
  static const routeName = '/profile';
  @override
  Widget build(BuildContext context) {

    Widget getInfoSection = Card(
      margin: const EdgeInsets.fromLTRB(15, 0, 15, 0),
      elevation: 0,
      child: Column(
        // mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Expanded(
              flex: 1,
              child: Column(
                children: [
                  Expanded(
                    flex: 5,
                    child: CircleAvatar(
                      backgroundImage: AssetImage('assets/avatar1.png'),
                      radius: 60,
                    ),
                  ),
                  Expanded(
                      flex: 2,
                      child: Text(
                        "Please enter your details",
                        style: TextStyle(
                          color: Colors.green.shade500,
                          fontSize: 20,
                        ),
                      )
                  )
                ],
              )
          ),
          Expanded(
            flex: 2,
            child: SingleChildScrollView(
              child : Column(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  _personalDetailInfo(0,  "assets/Icon awesome.png"),
                  _personalDetailInfo(1,  "assets/cake.png"),
                  _personalDetailInfo(2,  "assets/phone.png"),
                  _personalDetailInfo(3,  "assets/instagram.png"),
                  _personalDetailInfo(4,  "assets/mail.png"),
                  _personalDataInfoButton(context, userInputList),
                ],
              )
            ),
          )
        ],
      ),
    );

    return AnnotatedRegion<SystemUiOverlayStyle>(
      value: SystemUiOverlayStyle.dark,
      child : Stack (
        children : [
          Container(
            decoration: BoxDecoration(
              gradient: LinearGradient(
                  begin: Alignment.topLeft,
                  end: Alignment.bottomRight,
                  colors: [ Colors.white, Colors.green.shade200 ]
              ),
            ),
            child: Column(
              children: [
                Expanded(
                    flex: 2,
                    child: Container(
                        decoration: const BoxDecoration(
                            image: DecorationImage(
                                image: AssetImage('assets/robot-lookDown.png'),
                                fit: BoxFit.cover
                            )
                        )
                    )
                ),
                Expanded(
                  flex: 10,
                  child: Container(
                    margin: const EdgeInsets.fromLTRB(20, 0, 20, 50),
                    height: double.infinity,
                    width: double.infinity,
                    decoration: const BoxDecoration(
                        color: Colors.white,
                        borderRadius: BorderRadius.all(Radius.circular(8)),
                        boxShadow: [
                          BoxShadow(
                            color: Colors.grey,
                            spreadRadius: 1,
                            blurRadius: 3,
                            offset: Offset(0, 3),
                          )
                        ]
                    ),
                    child: getInfoSection,
                  ),
                )
              ],
            )
          ),
          Positioned(
          top: 48,
          right: 8,
          child: GestureDetector(
            onTap: () {
              Navigator.pop(context);
          },
          child: Image.asset(
              'assets/back_btn.png',
            width: 60,
            height: 60,
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _personalDetailInfo(int index, String imagePath) {
    TextEditingController controller = TextEditingController();
    String shadowText = '';
    switch (index) {
      case 0:
        shadowText = 'Enter Your Name';
        break;
      case 1:
        shadowText = 'Enter your birthdate';
        break;
      case 2:
        shadowText = 'Enter your phone number';
        break;
      case 3:
        shadowText = 'Enter your Instagram username';
        break;
      case 4:
        shadowText = 'Enter your email address';
        break;
    }

    return Container(
      margin: EdgeInsets.only(bottom: 10),
      child: Row(
        children: [
          Container(
            width: 24,
            height: 24,
            child: Image.asset(imagePath),
          ),
          SizedBox(width: 8),
          Expanded(
            child: TextFormField(
              controller: controller,
              onChanged: (value) {
                userInputList[index] = value;
              },
              decoration: InputDecoration(
                contentPadding:
                EdgeInsets.symmetric(vertical: 12, horizontal: 16),
                enabledBorder: const OutlineInputBorder(
                  borderSide: BorderSide(
                    width: 1,
                    color: Colors.lightGreen,
                  ),
                  borderRadius: BorderRadius.all(Radius.circular(5)),
                ),
                focusedBorder: const OutlineInputBorder(
                  borderSide: BorderSide(
                    width: 1,
                    color: Colors.green,
                  ),
                  borderRadius: BorderRadius.all(Radius.circular(10)),
                ),
                hintText: shadowText,
                hintStyle: TextStyle(
                  color: Colors.grey,
                  fontStyle: FontStyle.italic,
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  ElevatedButton _personalDataInfoButton(BuildContext context, List<String> userInputList) {
    return ElevatedButton(
      style: ButtonStyle(
        foregroundColor: MaterialStatePropertyAll(Colors.white),
        backgroundColor: MaterialStatePropertyAll(Colors.green.shade300),
        fixedSize: MaterialStatePropertyAll(Size(160, 50)),
        elevation: MaterialStatePropertyAll(3),
      ),
      onPressed: () {
        // Navigate to another page when the button is pressed
        Navigator.push(
          context,
          MaterialPageRoute(
              builder: (context) => View_ProfilePage(userInputList : userInputList)
          ),
        );
      },
      child: const Text(
        "SAVE",
        style: TextStyle(
          fontSize: 17,
          fontWeight: FontWeight.bold,
        ),
      ),
    );
  }

  void _saveUserInput(BuildContext context) {
    // Perform any validation or additional processing here before saving the input

    // Display the user inputs in a dialog
    showDialog(
      context: context,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('User Inputs'),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: List.generate(
              userInputList.length,
                  (index) => Text('${index + 1}. ${userInputList[index]}'),
            ),
          ),
          actions: [
            TextButton(
              onPressed: () {
                Navigator.pop(context);
              },
              child: const Text('OK'),
            ),
          ],
        );
      },
    );
  }
}

class View_ProfilePage extends StatelessWidget {
  final List<String> userInputList;

  View_ProfilePage({required this.userInputList});
  static const routeName = '/profile';
  @override
  Widget build(BuildContext context) {

    Widget getInfoSection = Card(
      margin: const EdgeInsets.fromLTRB(15, 0, 15, 0),
      elevation: 0,
      child: Column(
        // mainAxisAlignment: MainAxisAlignment.spaceEvenly,
        children: [
          Expanded(
              flex: 1,
              child: Column(
                children: [
                  Expanded(
                    flex: 5,
                    child: CircleAvatar(
                      backgroundImage: AssetImage('assets/avatar1.png'),
                      radius: 60,
                    ),
                  ),
                  Expanded(
                      flex: 2,
                      child: Text(
                        "Welcome To Profile Page",
                        style: TextStyle(
                          color: Colors.green.shade500,
                          fontSize: 20,
                        ),
                      )
                  )
                ],
              )
          ),
          Expanded(
            flex: 2,
            child: SingleChildScrollView(
                child : Column(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    _personalDetailInfo(userInputList[0],"assets/Icon awesome.png"),
                    _personalDetailInfo(userInputList[1], "assets/cake.png"),
                    _personalDetailInfo(userInputList[2], "assets/phone.png"),
                    _personalDetailInfo(userInputList[3], "assets/instagram.png"),
                    _personalDetailInfo(userInputList[4], "assets/mail.png"),
                    _personalDataInfoButton(),
                  ],
                )
            ),
          )
        ],
      ),
    );

    return AnnotatedRegion<SystemUiOverlayStyle>(
      value: SystemUiOverlayStyle.dark,
      child : Stack (
        children : [
          Container(
              decoration: BoxDecoration(
                gradient: LinearGradient(
                    begin: Alignment.topLeft,
                    end: Alignment.bottomRight,
                    colors: [ Colors.white, Colors.green.shade200 ]
                ),
              ),
              child: Column(
                children: [
                  Expanded(
                      flex: 2,
                      child: Container(
                          decoration: const BoxDecoration(
                              image: DecorationImage(
                                  image: AssetImage('assets/robot-lookDown.png'),
                                  fit: BoxFit.cover
                              )
                          )
                      )
                  ),
                  Expanded(
                    flex: 10,
                    child: Container(
                      margin: const EdgeInsets.fromLTRB(20, 0, 20, 50),
                      height: double.infinity,
                      width: double.infinity,
                      decoration: const BoxDecoration(
                          color: Colors.white,
                          borderRadius: BorderRadius.all(Radius.circular(8)),
                          boxShadow: [
                            BoxShadow(
                              color: Colors.grey,
                              spreadRadius: 1,
                              blurRadius: 3,
                              offset: Offset(0, 3),
                            )
                          ]
                      ),
                      child: getInfoSection,
                    ),
                  )
                ],
              )
          ),
          Positioned(
            top: 48,
            right: 8,
            child: GestureDetector(
              onTap: () {
                Navigator.pop(context);
              },
              child: Image.asset(
                'assets/back_btn.png',
                width: 60,
                height: 60,
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _personalDetailInfo(String value, String imagePath) {
    return Container(
      margin: EdgeInsets.only(bottom: 10), // Add margin of 8 pixels at the bottom
      child: Row(
        children: [
          Container(
            width: 24,
            height: 24,
            child : Image.asset(imagePath), // Image widget
          ),
          SizedBox(width: 8),
          Expanded(
            child : TextFormField(// Add a space between the image and the TextFormField
              readOnly: true,
              initialValue: value,
              decoration: InputDecoration(
                contentPadding: EdgeInsets.symmetric(vertical: 12, horizontal: 16),
                enabledBorder: const OutlineInputBorder(
                    borderSide: BorderSide(
                      width: 1, color: Colors.lightGreen,
                    ),
                    borderRadius: BorderRadius.all(Radius.circular(5))
                ),
                focusedBorder: const OutlineInputBorder(
                    borderSide: BorderSide(
                      width: 1, color: Colors.green,
                    ),
                    borderRadius: BorderRadius.all(Radius.circular(10))
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }

  ElevatedButton _personalDataInfoButton() {
    return ElevatedButton(
      style: ButtonStyle(
          foregroundColor: const MaterialStatePropertyAll(Colors.white),
          backgroundColor: MaterialStatePropertyAll(Colors.green.shade300),
          fixedSize: const MaterialStatePropertyAll(Size(160, 50)),
          elevation: const MaterialStatePropertyAll(3)
      ),
      onPressed: null, // TODO have to be implemented 'onPressed'
      child: const Text(
        "SAVE",
        style: TextStyle(
            fontSize: 17,
            fontWeight: FontWeight.bold
        ),
      ),
    );
  }
}
