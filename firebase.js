// Firebase v9+
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.6.1/firebase-app.js";
import { getAuth, createUserWithEmailAndPassword, signInWithEmailAndPassword, signOut } 
from "https://www.gstatic.com/firebasejs/9.6.1/firebase-auth.js";
import { getFirestore, doc, setDoc } 
from "https://www.gstatic.com/firebasejs/9.6.1/firebase-firestore.js";

// Your Firebase Config
const firebaseConfig = {
  apiKey: "AIzaSyA9or0xsb5RB-Z-JzntgFEGb51wK0b4w4Y",
  authDomain: "database-santri-e1240.firebaseapp.com",
  projectId: "database-santri-e1240",
  storageBucket: "database-santri-e1240.firebasestorage.app",
  messagingSenderId: "116390382568",
  appId: "1:116390382568:web:23ce25e5e3ba3e9087b25d",
  measurementId: "G-CPKGG6X5TD"
};

// Initialize Firebase
export const app = initializeApp(firebaseConfig);
export const auth = getAuth(app);
export const db = getFirestore(app);
