import React, { useState } from "react";
import { Home, Users, Zap, Settings, Edit, Save, X, Plus } from "lucide-react";

function Profile() {
  const [isEditing, setIsEditing] = useState(false);
  const [profile, setProfile] = useState({
    name: "Alex Johnson",
    location: "Mumbai",
    householdSize: 4,
    appliances: ["AC", "Geyser", "Fridge", "Lights", "TV", "Washing Machine"],
    energyGoal: "Save 20% this month"
  });

  const [tempProfile, setTempProfile] = useState({...profile});
  const [newAppliance, setNewAppliance] = useState("");

  const handleEdit = () => {
    setTempProfile({...profile});
    setIsEditing(true);
  };

  const handleSave = () => {
    setProfile({...tempProfile});
    setIsEditing(false);
  };

  const handleCancel = () => {
    setIsEditing(false);
  };

  const handleApplianceAdd = () => {
    if (newAppliance.trim()) {
      setTempProfile({
        ...tempProfile,
        appliances: [...tempProfile.appliances, newAppliance.trim()]
      });
      setNewAppliance("");
    }
  };

  const handleApplianceRemove = (index) => {
    const updatedAppliances = [...tempProfile.appliances];
    updatedAppliances.splice(index, 1);
    setTempProfile({
      ...tempProfile,
      appliances: updatedAppliances
    });
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-emerald-50 to-blue-50 p-6">
      <div className="max-w-4xl mx-auto">
        {/* Header with energy stats */}
        <div className="flex flex-col md:flex-row items-start md:items-center justify-between mb-8">
          <div>
            <h1 className="text-3xl font-bold text-gray-800">My Profile</h1>
            <p className="text-gray-600">Manage your household energy information</p>
          </div>
          
          {/* Energy savings badge */}
          <div className="bg-gradient-to-r from-emerald-500 to-teal-600 text-white px-4 py-2 rounded-full flex items-center mt-4 md:mt-0">
            <Zap size={18} className="mr-2" />
            <span className="font-medium">15% Energy Saved This Month</span>
          </div>
        </div>

        {/* Main content */}
        <div className="bg-white rounded-2xl shadow-lg overflow-hidden">
          {/* User info section */}
          <div className="relative p-6 md:p-8 border-b border-gray-100">
            {!isEditing && (
              <button 
                onClick={handleEdit} 
                className="absolute top-6 right-6 p-2 text-gray-500 hover:text-emerald-600 hover:bg-emerald-50 rounded-full transition-colors"
              >
                <Edit size={20} />
              </button>
            )}
            
            <div className="flex flex-col md:flex-row gap-6 items-start">
              {/* Avatar */}
              <div className="relative">
                <div className="w-24 h-24 rounded-full bg-gradient-to-br from-emerald-400 to-blue-500 flex items-center justify-center text-white text-2xl font-bold">
                  {profile.name.split(' ').map(n => n[0]).join('')}
                </div>
                {!isEditing && (
                  <div className="absolute -bottom-1 -right-1 bg-emerald-500 text-white p-1 rounded-full">
                    <Zap size={14} />
                  </div>
                )}
              </div>
              
              {/* User details */}
              <div className="flex-1">
                {isEditing ? (
                  <div className="space-y-4">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">Name</label>
                      <input 
                        type="text" 
                        value={tempProfile.name}
                        onChange={(e) => setTempProfile({...tempProfile, name: e.target.value})}
                        className="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-transparent"
                      />
                    </div>
                    
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">Location</label>
                      <input 
                        type="text" 
                        value={tempProfile.location}
                        onChange={(e) => setTempProfile({...tempProfile, location: e.target.value})}
                        className="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-transparent"
                      />
                    </div>
                    
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">Household Size</label>
                      <input 
                        type="number" 
                        value={tempProfile.householdSize}
                        onChange={(e) => setTempProfile({...tempProfile, householdSize: parseInt(e.target.value)})}
                        min="1"
                        className="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-transparent"
                      />
                    </div>
                    
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-1">Energy Goal</label>
                      <input 
                        type="text" 
                        value={tempProfile.energyGoal}
                        onChange={(e) => setTempProfile({...tempProfile, energyGoal: e.target.value})}
                        className="w-full p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-transparent"
                      />
                    </div>
                  </div>
                ) : (
                  <div>
                    <h2 className="text-2xl font-bold text-gray-800 mb-1">{profile.name}</h2>
                    <div className="flex items-center mb-4">
                      <Home size={16} className="text-gray-500 mr-1" />
                      <span className="text-gray-600">{profile.location}</span>
                      <Users size={16} className="text-gray-500 ml-4 mr-1" />
                      <span className="text-gray-600">{profile.householdSize} people</span>
                    </div>
                    <div className="inline-flex items-center px-3 py-1 bg-blue-50 text-blue-700 rounded-full">
                      <Zap size={14} className="mr-1" />
                      <span className="text-sm font-medium">Goal: {profile.energyGoal}</span>
                    </div>
                  </div>
                )}
              </div>
            </div>
          </div>
          
          {/* Appliances section */}
          <div className="p-6 md:p-8">
            <h3 className="text-lg font-semibold text-gray-800 mb-4 flex items-center">
              <Zap size={18} className="text-emerald-500 mr-2" />
              Registered Appliances
            </h3>
            
            {isEditing ? (
              <div className="space-y-4">
                <div className="flex gap-2 mb-4">
                  <input
                    type="text"
                    value={newAppliance}
                    onChange={(e) => setNewAppliance(e.target.value)}
                    placeholder="Add new appliance"
                    className="flex-1 p-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-emerald-500 focus:border-transparent"
                  />
                  <button
                    onClick={handleApplianceAdd}
                    className="p-2 bg-emerald-500 text-white rounded-lg hover:bg-emerald-600 transition-colors"
                  >
                    <Plus size={20} />
                  </button>
                </div>
                
                <div className="flex flex-wrap gap-2">
                  {tempProfile.appliances.map((appliance, index) => (
                    <div key={index} className="flex items-center bg-gray-100 rounded-full px-3 py-1">
                      <span className="text-gray-800">{appliance}</span>
                      <button 
                        onClick={() => handleApplianceRemove(index)}
                        className="ml-2 text-gray-500 hover:text-red-500"
                      >
                        <X size={16} />
                      </button>
                    </div>
                  ))}
                </div>
                
                <div className="flex gap-2 mt-6">
                  <button
                    onClick={handleSave}
                    className="flex items-center px-4 py-2 bg-emerald-500 text-white rounded-lg hover:bg-emerald-600 transition-colors"
                  >
                    <Save size={18} className="mr-2" />
                    Save Changes
                  </button>
                  <button
                    onClick={handleCancel}
                    className="px-4 py-2 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors"
                  >
                    Cancel
                  </button>
                </div>
              </div>
            ) : (
              <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
                {profile.appliances.map((appliance, index) => (
                  <div 
                    key={index} 
                    className="flex items-center justify-center p-4 bg-gray-50 border border-gray-100 rounded-xl hover:shadow-md transition-shadow"
                  >
                    <span className="font-medium text-gray-700">{appliance}</span>
                  </div>
                ))}
              </div>
            )}
          </div>
          
          {/* Energy tips */}
          <div className="p-6 md:p-8 bg-gradient-to-r from-emerald-50 to-blue-50">
            <h3 className="text-lg font-semibold text-gray-800 mb-4">Your Energy Tip</h3>
            <div className="bg-white p-4 rounded-xl shadow-sm border border-emerald-100">
              <p className="text-gray-700">
                <span className="font-medium text-emerald-600">Pro tip:</span> Based on your profile, you could save up to 15% by optimizing your AC's temperature settings. Try setting it to 24°C for optimal comfort and efficiency.
              </p>
            </div>
          </div>
        </div>
        
        {/* Settings link */}
        <div className="flex justify-end mt-6">
          <a href="#" className="flex items-center text-gray-600 hover:text-emerald-600">
            <Settings size={18} className="mr-1" />
            <span>Advanced Energy Settings</span>
          </a>
        </div>
      </div>
    </div>
  );
}

export default Profile;