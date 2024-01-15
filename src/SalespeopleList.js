import React, { useState, useEffect }  from "react";


function SalespeopleList() {
    const [salesperson, setSalesperson] = useState([]);

    const baseUrl = process.env.NODE_ENV === 'production'
    ? 'https://dealer-dashboard-8d7b3aea3ae7.herokuapp.com/'
    : 'http://localhost:8090/';

    // Postman shows 200 OK

    async function LoadSalespeople() {
        const response = await fetch(`${baseUrl}salespeople/`);
        if (response.ok) {
            const data = await response.json();
            setSalesperson(data.salesperson)
        }
    }

    useEffect(() => {
        LoadSalespeople();
    }, []);

    return (
        <div>
            <h1>Salespeople</h1>
            <table className="table table-striped">
                <thead>
                    <tr>
                        <th>Employee ID</th>
                        <th>First Name</th>
                        <th>Last Name</th>
                    </tr>
                </thead>
                <tbody>
                    {salesperson.map((salespersonData) => {
                        return (
                            <tr key={salespersonData.id}>
                                <td>{ salespersonData.employee_id }</td>
                                <td>{ salespersonData.first_name }</td>
                                <td>{ salespersonData.last_name }</td>
                            </tr>
                        )
                    })}
                </tbody>
            </table>
        </div>
    );
}

export default SalespeopleList;
