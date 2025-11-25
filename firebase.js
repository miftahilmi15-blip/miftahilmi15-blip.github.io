// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyAQ1A9rtEoEYoriA5Y7oSB84Fd1Xnu6aes",
  authDomain: "e-santri-ed555.firebaseapp.com",
  projectId: "e-santri-ed555",
  storageBucket: "e-santri-ed555.firebasestorage.app",
  messagingSenderId: "588687778472",
  appId: "1:588687778472:web:11ee425d3c8e5d17d2189d",
  measurementId: "G-18H1ECWW86"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);
