import React, { useState, useEffect }  from "react";


export default function ManufacturerList() {
    const [manufacturer, setManufacturer] = useState([]);

    const baseUrl = process.env.NODE_ENV === 'production'
    ? 'https://dealer-dashboard-8d7b3aea3ae7.herokuapp.com/'
    : 'http://localhost:8100/';

    async function LoadManufacturer() {
        // Postman shows 200 OK
        const response = await fetch(`${baseUrl}manufacturers/`);
        if (response.ok) {
          const data = await response.json();
          setManufacturer(data.manufacturers);
        }
      }

    useEffect(() => {
        LoadManufacturer();
    }, []);


    return (
        <div>
            <h1>Manufacturers</h1>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Name</th>
                    </tr>
                </thead>
                <tbody>
                    {manufacturer.map((manufacturerData) => {
                        return (
                            <tr key={manufacturerData.id}>
                                <td>{ manufacturerData.name }</td>
                            </tr>
                        )
                    })}
                </tbody>
            </table>
        </div>
    );
}
