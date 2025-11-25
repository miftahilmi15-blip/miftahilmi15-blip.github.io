// firebase.js - initialized with user's config
// Replace these values only if you change project
var firebaseConfig = {
  apiKey: "AIzaSyA9or0xsb5RB-Z-JzntgFEGb51wK0b4w4Y",
  authDomain: "database-santri-e1240.firebaseapp.com",
  projectId: "database-santri-e1240",
  storageBucket: "database-santri-e1240.firebasestorage.app",
  messagingSenderId: "116390382568",
  appId: "1:116390382568:web:23ce25e5e3ba3e9087b25d",
  measurementId: "G-CPKGG6X5TD"
};
// Initialize Firebase (compat)
firebase.initializeApp(firebaseConfig);
var auth = firebase.auth();
var db = firebase.firestore();
