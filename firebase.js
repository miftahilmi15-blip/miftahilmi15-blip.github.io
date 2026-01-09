
const firebaseConfig = {
  apiKey: "AIzaSyAQ1A9rtEoEYoriA5Y7oSB84Fd1Xnu6aes",
  authDomain: "e-santri-ed555.firebaseapp.com",
  projectId: "e-santri-ed555",
  storageBucket: "e-santri-ed555.appspot.com",
  messagingSenderId: "588687778472",
  appId: "1:588687778472:web:3000ae9b18f1004ed2189d",
  measurementId: "G-MB8M1EGFJS"
};

// Init
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.firestore();
