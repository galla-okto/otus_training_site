import axios from "axios";
const url = "http://127.0.0.1:8000/myapi/api/clients/";

axios({
    method: "get",
    url
  }).then((response) => console.log(response.data));

const url_workouts = "http://127.0.0.1:8000/myapi/api/workouts/";

fetch(url_workouts)
    .then((response) => response.json())
    .then((data) => console.log(data));
