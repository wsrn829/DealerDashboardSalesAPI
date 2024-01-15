import React, { useState } from "react";

export default function ManufacturerForm() {
  const [name, setName] = useState("");

  const handleName = (event) => {
    const value = event.target.value;
    setName(value);
  };

  const data = {
    name: name,

  };

  const baseUrl = process.env.NODE_ENV === 'production'
    ? 'https://dealer-dashboard-8d7b3aea3ae7.herokuapp.com/'
    : 'http://localhost:8100/';

  // Postman shows 200 OK
  const manufacturerURL = `${baseUrl}manufacturers/`;
  const fetchConfig = {
    method: "post",
    body: JSON.stringify(data),
    headers: {
      "Content-Type": "application/json",
    },
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const response = await fetch(manufacturerURL, fetchConfig);
    if (response.ok) {
      // const newManufacturer = await response.json();
      setName("");
    }
  };



  return (
    <div>
      <div className="my-5 container">
        <div className="row">
          <div className="offset-3 col-6">
            <div className="shadow p-4 mt-4">
              <h1>Create a manufacturer</h1>
              <form onSubmit={handleSubmit} id="create-salesperson-form">
                <div className="form-floating mb-3">
                  <input
                    value={name} onChange={handleName} placeholder="Name" required type="text" name="name" id="name" className="form-control"
                  />
                  <label htmlFor="name">Manufacturer Name</label>
                </div>
                <button className="btn btn-primary">Create</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}
