id = null;

document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    url_to_api = "http://127.0.0.1:5000/api"

    // Simulate login process
    if (username && password) {
        login(username, password);
    } else {
        alert('Please enter both username and password.');
    }
});

function get_devices(user_id) {
    fetch(url_to_api + '/brockers/getuser/' + user_id, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Failed to fetch devices');
        }
        return response.json();
    })
    .then(devices => {
        const deviceList = document.getElementById('device-list'); // Assuming there's a <ul> or <div> with id="device-list"
        deviceList.innerHTML = ''; // Clear previous content


        //------------------------------------------------------------------------------------

        devices.forEach(device => {
            const listItem = document.createElement('li'); // Create a list item for each device
            listItem.textContent = `${device.name} (Data:\n${device.type} | ${device.topic})`; // Display device name and type

            // Create an edit button
            const editButton = document.createElement('button');
            editButton.textContent = 'Edit';
            editButton.style.marginLeft = '10px'; // Add some spacing
            editButton.addEventListener('click', () => {
                // Open a modal or prompt for editing
                const newName = prompt('Enter new name:', device.name);
                const newType = prompt('Enter new type:', device.type);
                const newLocation = prompt('Enter new location:', device.location_id);
                const newTopic = prompt('Enter new topic:', device.topic);

                if (newName && newType) {
                    // Send PUT request to update the device
                    fetch(`${url_to_api}/devices/${device.id}`, {
                        method: 'PUT',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ 
                            'name': newName, 
                            'type': newType, 
                            'location_id': newLocation, 
                            'topic': newTopic 
                        })
                    })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Failed to update device');
                        }
                        return response.json();
                    })
                    .then(updatedDevice => {
                        alert('Device updated successfully!');
                        listItem.textContent = `${updatedDevice.name} (${updatedDevice.type})`; // Update the list item text
                        listItem.appendChild(editButton); // Re-append the edit button
                        listItem.appendChild(deleteButton); // Re-append the delete button
                    })
                    .catch(error => {
                        console.error('Error updating device:', error);
                        alert('Failed to update device.');
                    });
                }
            });

            // Create a delete button
            const deleteButton = document.createElement('button');
            deleteButton.textContent = 'Delete';
            deleteButton.style.marginLeft = '10px'; // Add some spacing
            deleteButton.addEventListener('click', () => {
                if (confirm(`Are you sure you want to delete ${device.name}?`)) {
                    // Send DELETE request to remove the device
                    fetch(`${url_to_api}/devices/${device.id}`, {
                        method: 'DELETE',
                        headers: {
                            'Content-Type': 'application/json'
                        }
                    })
                    .then(response => {
                        if (!response.ok) {
                            throw new Error('Failed to delete device');
                        }
                        alert('Device deleted successfully!');
                        deviceList.removeChild(listItem); // Remove the list item from the UI
                    })
                    .catch(error => {
                        console.error('Error deleting device:', error);
                        alert('Failed to delete device.');
                    });
                }
            });

            listItem.appendChild(editButton); // Append the edit button to the list item
            listItem.appendChild(deleteButton); // Append the delete button to the list item
            deviceList.appendChild(listItem); // Append the item to the list
        });

        //------------------------------------------------------------------------------------
    })
    .catch(error => {
        console.error('Error fetching devices:', error);
        alert('Failed to load devices.');
    });
}

function login(username, password) {
    fetch(url_to_api + '/brockers/aut', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => {
        if (!response.ok) {
            alert('Authorization failed');
            throw new Error('Authorization failed');

        }
        return response.json();
    })
    .then(data => {
        console.log('User ID:', data.id);
        id = data.id;
        document.getElementById('login-section').style.display = 'none';
        document.getElementById('device-section').style.display = 'block';
        get_devices(id); // Fetch devices for the logged-in user
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Authorization failed ' + error);
    });
}

// document.getElementById('create-device-button').addEventListener('click', () => {
//     const name = prompt('Enter device name:');
//     const type = prompt('Enter device type:');
//     const location_id = prompt('Enter location ID:');
//     const topic = prompt('Enter topic:');

//     if (name && type && location_id && topic) {
//         // Send POST request to create a new device
//         fetch(`${url_to_api}/devices`, {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json'
//             },
//             body: JSON.stringify({
//                 name: name,
//                 type: type,
//                 location_id: location_id,
//                 topic: topic
//             })
//         })
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error('Failed to create device');
//             }
//             return response.json();
//         })
//         .then(newDevice => {
//             fetch(url_to_api + '/brockers/addDevice', {
//                 method: 'PUT',
//                 headers: {
//                     'Content-Type': 'application/json'
//                 },
//                 body: JSON.stringify({ 'user_id': id, 'device_id': newDevice.id })
//             })
//             get_devices(id);
//             alert('Device created successfully!');
            

//             const deleteButton = document.createElement('button');
//             deleteButton.textContent = 'Delete';
//             deleteButton.style.marginLeft = '10px';
//             deleteButton.addEventListener('click', () => {
//                 // Delete functionality (reuse existing code)
//             });

//             listItem.appendChild(editButton);
//             listItem.appendChild(deleteButton);
//             deviceList.appendChild(listItem);
//         })
//         .catch(error => {
//             console.error('Error creating device:', error);
//             alert('Failed to create device.');
//         });
//     } else {
//         alert('All fields are required to create a device.');
//     }
// });


//##########################################################

document.getElementById('create-device-button').addEventListener('click', () => {
    const name = prompt('Enter device name:');
    const type = prompt('Enter device type:');
    const location_id = prompt('Enter location ID:');
    const topic = prompt('Enter topic:');

    if (name && type && location_id && topic) {
        // Send POST request to create a new device
        fetch(`${url_to_api}/devices`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                name: name,
                type: type,
                location_id: location_id,
                topic: topic
            })
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Failed to create device');
            }
            return response.json();
        })
        .then(newDevice => {
            // Add the new device to the user's list on the server
            fetch(`${url_to_api}/brockers/addDevice`, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ 'user_id': id, 'device_id': newDevice.id })
            })
            .then(() => {
                // Dynamically add the new device to the UI
                const deviceList = document.getElementById('device-list');
                const listItem = document.createElement('li');
                listItem.textContent = `${newDevice.name} (${newDevice.type})`;

                // Create edit and delete buttons
                const editButton = document.createElement('button');
                editButton.textContent = 'Edit';
                editButton.style.marginLeft = '10px';
                editButton.addEventListener('click', () => {
                    const newName = prompt('Enter new name:', newDevice.name);
                    const newType = prompt('Enter new type:', newDevice.type);

                    if (newName && newType) {
                        fetch(`${url_to_api}/devices/${newDevice.id}`, {
                            method: 'PUT',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({ name: newName, type: newType })
                        })
                        .then(response => {
                            if (!response.ok) {
                                throw new Error('Failed to update device');
                            }
                            return response.json();
                        })
                        .then(updatedDevice => {
                            alert('Device updated successfully!');
                            listItem.textContent = `${updatedDevice.name} (${updatedDevice.type})`;
                            listItem.appendChild(editButton);
                            listItem.appendChild(deleteButton);
                        })
                        .catch(error => {
                            console.error('Error updating device:', error);
                            alert('Failed to update device.');
                        });
                    }
                });

                const deleteButton = document.createElement('button');
                deleteButton.textContent = 'Delete';
                deleteButton.style.marginLeft = '10px';
                deleteButton.addEventListener('click', () => {
                    if (confirm(`Are you sure you want to delete ${newDevice.name}?`)) {
                        fetch(`${url_to_api}/devices/${newDevice.id}`, {
                            method: 'DELETE',
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        })
                        .then(response => {
                            if (!response.ok) {
                                throw new Error('Failed to delete device');
                            }
                            alert('Device deleted successfully!');
                            deviceList.removeChild(listItem);
                        })
                        .catch(error => {
                            console.error('Error deleting device:', error);
                            alert('Failed to delete device.');
                        });
                    }
                });

                listItem.appendChild(editButton);
                listItem.appendChild(deleteButton);
                deviceList.appendChild(listItem);
                alert('Device created successfully!');
            })
            .catch(error => {
                console.error('Error adding device to user:', error);
                alert('Failed to add device to user.');
            });
        })
        .catch(error => {
            console.error('Error creating device:', error);
            alert('Failed to create device.');
        });
    } else {
        alert('All fields are required to create a device.');
    }
});