# QuickComs - AI-Powered Team Communication Analytics Platform

An intelligent system that transforms fragmented team communications into actionable insights, visual workflows, and professional content for mid-size startups struggling with cross-team visibility.

## Problem Statement

Mid-size startups face a critical challenge: as teams grow beyond 20-50 people, communication becomes siloed and leadership loses visibility into day-to-day progress. Engineering, Finance, Product, and Operations teams work in isolation, leading to:

- **Information asymmetry** between leadership and individual contributors
- **Duplicated efforts** across teams due to poor communication
- **Delayed decision-making** from lack of real-time progress visibility
- **Investor relations challenges** when creating coherent progress narratives
- **Onboarding difficulties** for new team members understanding workflows

QuickComs solves this by automatically processing distributed team communications and generating comprehensive insights that scale with organizational growth.

## Solution Architecture

QuickComs implements a sophisticated AI-driven pipeline that processes unstructured team communications and produces multiple output formats:

**Core Capabilities:**
- **Intelligent Categorization**: Machine learning-based classification of communications by team and project context
- **Workflow Visualization**: Automated generation of process flowcharts from conversation patterns
- **Content Synthesis**: AI-powered creation of executive summaries and stakeholder updates
- **Multimedia Generation**: Professional video content with synchronized narration for presentations

**Technical Implementation:**
- **Natural Language Processing**: OpenAI GPT models for semantic understanding and content generation
- **Data Pipeline Architecture**: Scalable processing system handling multiple input formats
- **Real-time API Services**: RESTful endpoints for integration with existing tools
- **Multi-modal Output**: Charts, videos, and structured reports for different stakeholder needs

## Key Features

### AI-Powered Processing Engine
- Advanced team categorization using OpenAI GPT-3.5 and GPT-4
- Context-aware flowchart generation from conversation logs
- Customizable social media content creation with tone adaptation
- Semantic analysis of communication patterns and bottlenecks

### Visual Analytics Dashboard
- Dynamic Mermaid flowcharts representing team workflow sequences
- High-resolution PNG exports optimized for presentations
- Real-time chart serving through dedicated API endpoints
- Interactive visualization of cross-team dependencies

### Professional Video Generation
- Enterprise-grade text-to-speech using ElevenLabs neural voices
- Automated video assembly with MoviePy for consistent branding
- Synchronized audio narration with visual slide presentations
- Intelligent keyword highlighting for technical terminology

### Enterprise Data Integration
- Native Supabase PostgreSQL database connectivity
- Flexible JSON/CSV file processing capabilities
- Direct text file ingestion for legacy systems
- RESTful API architecture for third-party integrations

## Technical Requirements

### System Prerequisites
- Python 3.8+ with pip package manager
- Node.js runtime environment (for Mermaid CLI toolchain)
- API credentials for OpenAI and ElevenLabs services
- PostgreSQL database access (Supabase recommended)

### Installation and Setup

1. **Repository Setup**
```bash
git clone <repository-url>
cd quickcoms
```

2. **Python Environment Configuration**
```bash
pip install -r requirements.txt
```

3. **Mermaid CLI Installation**
```bash
npm install -g @mermaid-js/mermaid-cli
```

4. **Environment Configuration**
```bash
cp .env.example .env
# Configure with your service credentials
```

Required environment variables:
```env
OPENAI_API_KEY=your_openai_api_key
ELEVENLABS_API_KEY=your_elevenlabs_api_key
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
```

### Pipeline Execution

**Complete Processing Pipeline:**
```bash
python run_pipeline.py
```

**Modular Execution (for development and debugging):**
```bash
# Data ingestion and preprocessing
python steps/json_to_txt/convert_to_txt.py

# AI-powered team categorization
python steps/categorize/categorize_txt_to_team.py

# Workflow visualization generation
python steps/generate/generate_mermaid_charts.py

# Image rendering and export
python steps/generate/convert_mmd_to_png.py
```

**Multimedia Content Generation:**
```bash
# Neural voice synthesis
python steps/video_generation/text_to_speech.py

# Professional video assembly
python steps/video_generation/generate_weekly_videos.py
```

**Production Services:**
```bash
# Primary API server (content generation)
uvicorn main:app --reload --port 8000

# Chart serving microservice
uvicorn chart_server:app --reload --port 8001
```

## System Architecture

```
quickcoms/
├── main.py                 # FastAPI server for content generation
├── chart_server.py         # Chart serving API
├── run_pipeline.py         # Main pipeline orchestrator
├── supabase_client.py      # Database connection
├── steps/                  # Processing pipeline
│   ├── json_to_txt/       # Data conversion
│   ├── categorize/        # AI team classification
│   ├── generate/          # Chart generation
│   ├── video_generation/  # Video creation
│   └── supabase_fetch/    # Database queries
├── logs_txt/              # Input text files
├── team_logs/             # Categorized logs
├── flowcharts/            # Generated charts (.mmd & .png)
├── voiceovers/            # Audio files (.mp3)
└── videos/                # Final videos (.mp4)
```

## Data Processing Pipeline

The system implements a sophisticated multi-stage processing pipeline:

1. **Data Ingestion**: Automated collection from Supabase, JSON, CSV, and text sources
2. **Semantic Analysis**: AI-powered categorization using OpenAI GPT models for team assignment
3. **Workflow Extraction**: GPT-4 processes communication patterns to generate Mermaid flowcharts
4. **Visual Rendering**: Mermaid CLI converts diagrams to high-resolution PNG images
5. **Audio Synthesis**: ElevenLabs neural networks generate professional voiceovers
6. **Video Production**: MoviePy assembles synchronized multimedia presentations

## API Documentation

### Primary Content Generation Service (Port 8000)
- `POST /generate-post/` - Generate contextual social media content from uploaded team updates
- `GET /test-insert` - Database connectivity validation and health check

### Chart Visualization Service (Port 8001)
- `GET /chart/{team_name}` - Serve dynamically generated team workflow visualizations

## Supported Data Formats

### JSON Format
```json
{
  "channels": [
    {
      "name": "engineering",
      "messages": [
        {"text": "Fixed the API endpoint bug."},
        {"text": "Refactored the DB schema."}
      ]
    }
  ]
}
```

### CSV Format
```csv
log,team
"Fixed API bug",engineering
"Reviewed Q1 expenses",finance
```

### Text Files
Place `.txt` files in `logs_txt/` folder with team-specific content.

## Configuration Management

### Team Classification Schema
Default organizational units: `Tech`, `Finance`, `Engineering`, `Product`
Customizable via `steps/categorize/categorize_txt_to_team.py`

### Video Production Parameters
- Output resolution: 1280x720 (HD)
- Slide duration: 4 seconds per segment
- Typography: 48px professional font rendering
- Keyword highlighting: Configurable technical terminology

### Neural Voice Synthesis
- Model: `eleven_monolingual_v1` (ElevenLabs)
- Voice stability: 0.3 (natural variation)
- Similarity boost: 0.7 (consistent quality)

## Business Applications

### Executive Reporting
- Automated weekly progress videos for investor relations
- Cross-functional team performance analytics and trend identification
- Executive dashboard integration with real-time workflow visualization

### Operational Intelligence
- Communication pattern analysis for process optimization
- Bottleneck identification across engineering and product teams
- Resource allocation insights based on team activity patterns

### Content Marketing
- Automated social media content generation from development updates
- Professional presentation materials for stakeholder meetings
- Technical documentation and process flowchart generation

### Organizational Development
- New employee onboarding with visual workflow documentation
- Cross-team collaboration analysis and improvement recommendations
- Knowledge management through automated conversation summarization

## Development and Contribution

### Contributing Guidelines
1. Fork the repository and create a feature branch
2. Implement changes with comprehensive testing
3. Ensure code quality standards and documentation
4. Submit pull request with detailed change description

### Technical Validation
- Verify environment configuration in `.env.example`
- Confirm API service connectivity and authentication
- Test Mermaid CLI installation: `mmdc --version`
- Validate Python dependencies and version compatibility

## License

MIT License - see LICENSE file for complete terms and conditions

## Technical Support

For implementation questions or troubleshooting:
- Review the issues page for documented solutions
- Verify all required environment variables are configured
- Ensure proper API key authentication for external services
- Confirm system prerequisites and dependency versions

---

**Engineered for mid-size startups seeking scalable team communication insights**