from enum import Enum
from typing import List, Dict, Tuple

class ProjectRole(str, Enum):
    """Define valid project roles."""
    PERDAMAN_MANAGEMENT = 'perdaman_management'
    PERDAMAN_ENV_HERITAGE_MANAGER = 'perdaman_env_heritage_manager'
    SCJV_PROJECT_DIRECTOR = 'scjv_project_director'
    SCJV_PROJECT_MANAGER = 'scjv_project_manager'
    SCJV_CONSTRUCTION_MANAGER = 'scjv_construction_manager'
    SCJV_COMMERCIAL_MANAGER = 'scjv_commercial_manager'
    SCJV_ENGINEERING_MANAGER = 'scjv_engineering_manager'
    SCJV_ENVIRONMENTAL_LEAD = 'scjv_environmental_lead'
    SCJV_HSSE_MANAGER = 'scjv_hsse_manager'
    SCJV_HERITAGE_INDIGENOUS_MANAGER = 'scjv_heritage_indigenous_manager'
    SCJV_LEAD_ENV_ADVISOR = 'scjv_lead_env_advisor'
    SCJV_SENIOR_ENV_ADVISOR = 'scjv_senior_env_advisor'
    SCJV_CONSTRUCTION_DIRECTOR = 'scjv_construction_director'
    SCJV_PROJECT_ENV_REPRESENTATIVE = 'scjv_project_env_representative'
    SCJV_CONSTRUCTION_SUPERVISOR = 'scjv_construction_supervisor'
    SCJV_COMMUNITY_STAKEHOLDER = 'scjv_community_stakeholder'

    # Original roles for backward compatibility
    OWNER = 'owner'
    MANAGER = 'manager'
    MEMBER = 'member'
    VIEWER = 'viewer'

# Map of internal role values to human-readable display names
ROLE_DISPLAY_NAMES: Dict[str, str] = {
    ProjectRole.PERDAMAN_MANAGEMENT.value: 'Perdaman - Management',
    ProjectRole.PERDAMAN_ENV_HERITAGE_MANAGER.value: 'Perdaman - Env & Heritage Manager',
    ProjectRole.SCJV_PROJECT_DIRECTOR.value: 'SCJV - Project Director',
    ProjectRole.SCJV_PROJECT_MANAGER.value: 'SCJV - Project Manager',
    ProjectRole.SCJV_CONSTRUCTION_MANAGER.value: 'SCJV - Construction Manager',
    ProjectRole.SCJV_COMMERCIAL_MANAGER.value: 'SCJV - Commercial Manager',
    ProjectRole.SCJV_ENGINEERING_MANAGER.value: 'SCJV - Engineering Manager',
    ProjectRole.SCJV_ENVIRONMENTAL_LEAD.value: 'SCJV - Environmental Lead',
    ProjectRole.SCJV_HSSE_MANAGER.value: 'SCJV - HSSE Manager',
    ProjectRole.SCJV_HERITAGE_INDIGENOUS_MANAGER.value: 'SCJV - Heritage & Indigenous Relations Manager',
    ProjectRole.SCJV_LEAD_ENV_ADVISOR.value: 'SCJV - Lead Environmental Advisor',
    ProjectRole.SCJV_SENIOR_ENV_ADVISOR.value: 'SCJV - Senior Environmental Advisor',
    ProjectRole.SCJV_CONSTRUCTION_DIRECTOR.value: 'SCJV - Construction Director',
    ProjectRole.SCJV_PROJECT_ENV_REPRESENTATIVE.value: 'SCJV - Project Environmental Representative',
    ProjectRole.SCJV_CONSTRUCTION_SUPERVISOR.value: 'SCJV - Construction Supervisor',
    ProjectRole.SCJV_COMMUNITY_STAKEHOLDER.value: 'SCJV - Community and Stakeholder',

    # Original roles with title-cased display names
    ProjectRole.OWNER.value: 'Owner',
    ProjectRole.MANAGER.value: 'Manager',
    ProjectRole.MEMBER.value: 'Member',
    ProjectRole.VIEWER.value: 'Viewer',
}

def get_role_choices() -> List[Tuple[str, str]]:
    """
    Get choices for model field with human-readable display names.

    Returns:
        List[Tuple[str, str]]: List of tuples (role_value, display_name)
    """
    return [(role.value, ROLE_DISPLAY_NAMES[role.value]) for role in ProjectRole]

def get_responsibility_choices() -> List[Tuple[str, str]]:
    """
    Get choices for the responsibility field in Obligation model.
    Uses display names as values for backward compatibility.

    Returns:
        List[Tuple[str, str]]: List of tuples (display_name, display_name)
    """
    # For the responsibility field, both the key and value are the display name
    # This maintains compatibility with existing data
    return [(display_name, display_name) for _, display_name in get_role_choices()
            if display_name not in ['Owner', 'Manager', 'Member', 'Viewer']]

def get_role_from_responsibility(responsibility: str) -> str:
    """
    Convert a responsibility display name to its corresponding role value.

    Args:
        responsibility (str): The display name of the responsibility

    Returns:
        str: The corresponding role value or None if not found
    """
    inverse_map = {display: value for value, display in get_role_choices()}
    return inverse_map.get(responsibility)

def get_responsibility_from_role(role: str) -> str:
    """
    Convert a role value to its corresponding responsibility display name.

    Args:
        role (str): The role value

    Returns:
        str: The corresponding responsibility display name or None if not found
    """
    return ROLE_DISPLAY_NAMES.get(role)
